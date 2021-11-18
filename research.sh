curl 'https://gaming.amazon.com/graphql' \
	-X POST \
	-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0' \
	--compressed \
	-H 'Content-Type: application/json' \
	-H 'csrf-token: giVjMeRMVxJHvZ9SY7dlVukBuIVDFOux3izl838AAAACAAAAAGGVpNJyYXcAAAAA+8jokd9rqj+wHxPcX6iU' \
	-H 'Cookie: session-id=146-8168887-4057637; session-id-time=2082787201l; ubid-main=130-3016880-8935116' \
	--data-raw '{"operationName":"OffersContext_Offers","variables":{},"query":"query OffersContext_Offers($dateOverride: Time) {\n  primeOffers(dateOverride: $dateOverride) {\n    ...PrimeOffer\n    __typename\n  }\n}\n\nfragment PrimeOfferAssets_Pixels on PrimeOfferAssets {\n  id\n  pixels {\n    ...Pixel\n    __typename\n  }\n  __typename\n}\n\nfragment PrimeOffer on PrimeOffer {\n  catalogId\n  id\n  title\n  assets {\n    type\n    purpose\n    location\n    location2x\n    __typename\n  }\n  offerAssets {\n    ...PrimeOfferAssets_Pixels\n    __typename\n  }\n  description\n  deliveryMethod\n  isRetailLinkOffer\n  priority\n  tags {\n    type\n    tag\n    __typename\n  }\n  content {\n    externalURL\n    publisher\n    categories\n    __typename\n  }\n  startTime\n  endTime\n  self {\n    claimInstructions\n    orderInformation {\n      ...PrimeOfferOrderInformation\n      __typename\n    }\n    eligibility {\n      ...PrimeOfferEligibility\n      __typename\n    }\n    __typename\n  }\n  linkedJourney {\n    ...LinkedJourney\n    __typename\n  }\n  __typename\n}\n\nfragment PrimeOfferEligibility on OfferEligibility {\n  isClaimed\n  canClaim\n  isPrimeGaming\n  missingRequiredAccountLink\n  offerStartTime\n  offerEndTime\n  offerState\n  gameAccountDisplayName\n  inRestrictedMarketplace\n  maxOrdersExceeded\n  conflictingClaimAccount {\n    ...ConflictingClaimAccount\n    __typename\n  }\n  __typename\n}\n\nfragment LinkedJourney on Journey {\n  offers {\n    ...LinkedJourneyOffer\n    __typename\n  }\n  __typename\n}\n\nfragment LinkedJourneyOffer on JourneyOffer {\n  catalogId\n  grantsCode\n  self {\n    eligibility(getOnlyActiveOffers: true) {\n      canClaim\n      isClaimed\n      conflictingClaimAccount {\n        ...ConflictingClaimAccount\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PrimeOfferOrderInformation on OfferOrderInformation {\n  orderDate\n  orderState\n  claimCode\n  __typename\n}\n\nfragment Pixel on Pixel {\n  type\n  pixel\n  __typename\n}\n\nfragment ConflictingClaimAccount on ConflictingClaimUser {\n  fullName\n  obfuscatedEmail\n  __typename\n}\n","extensions":{}}' | jq '.data.primeOffers[]'

# id: string
# title: string
# description: string
# startTime: string
# endTime: string
# content.externalURL: string | null
