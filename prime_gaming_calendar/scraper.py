from requests import Session
from typing import Dict, Any, List
from selectolax.parser import HTMLParser

JSONObject = Dict[str, Any]

QUERY = """query OffersContext_Offers($dateOverride: Time) {
	primeOffers(dateOverride: $dateOverride) {
			...PrimeOffer
			__typename
		}
	}
		
	fragment PrimeOfferAssets_Pixels on PrimeOfferAssets {
		id
		pixels {
			...Pixel
			__typename
			}
		__typename
	}
	
	fragment PrimeOffer on PrimeOffer {
		catalogId
		id
		title
		assets {
			type
			purpose
			location
			location2x
			__typename
		}
		offerAssets {
			...PrimeOfferAssets_Pixels
			__typename
		}
		description
		deliveryMethod
		isRetailLinkOffer
		priority
		tags {
			type
			tag
			__typename
		}
		content {
			externalURL
			publisher
			categories
			__typename
		}
		startTime
		endTime
		self {
			claimInstructions
			orderInformation {
				...PrimeOfferOrderInformation
				__typename
			}
			eligibility {
				...PrimeOfferEligibility
				__typename
			}
			__typename
		}
		linkedJourney {
			...LinkedJourney
			__typename
		}
		__typename
	}
	
	fragment PrimeOfferEligibility on OfferEligibility {
		isClaimed
		canClaim
		isPrimeGaming
		missingRequiredAccountLink
		offerStartTime
		offerEndTime
		offerState
		gameAccountDisplayName
		inRestrictedMarketplace
		maxOrdersExceeded
		conflictingClaimAccount {
			...ConflictingClaimAccount
			__typename
		}
		__typename
	}
	
	fragment LinkedJourney on Journey {
		offers {
			...LinkedJourneyOffer
			__typename
		}
		__typename
	}
	
	fragment LinkedJourneyOffer on JourneyOffer {
		catalogId
		grantsCode
		self {
			eligibility(getOnlyActiveOffers: true) {
				canClaim
				isClaimed
				conflictingClaimAccount {
						...ConflictingClaimAccount
						__typename
					}
					__typename
				}
				__typename
			}
			__typename
	}
	
	fragment PrimeOfferOrderInformation on OfferOrderInformation {
		orderDate
		orderState
		claimCode
		__typename
	}
	
	fragment Pixel on Pixel {
		type
		pixel
		__typename
	}
	
	fragment ConflictingClaimAccount on ConflictingClaimUser {
		fullName
		obfuscatedEmail
		__typename
	}
"""

session = Session()
session.headers["User-Agent"] = 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'

def get_csrf_token() -> str:
	res = session.get("https://gaming.amazon.com/home")
	res.raise_for_status()
	text = res.text
	tree = HTMLParser(text)
	return tree.css_first("input[name=csrf-key]").attributes["value"]

def get_offers() -> List[JSONObject]:
	res = session.post(
		'https://gaming.amazon.com/graphql',
		headers={
			"csrf-token": get_csrf_token(),
		},
		json={
			"operationName": "OffersContext_Offers",
			"variables": {},
			"query": QUERY,
			"extensions": {}
		}
	)
	res.raise_for_status()
	
	return res.json()["data"]["primeOffers"]
