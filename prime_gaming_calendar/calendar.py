from datetime import datetime
from icalendar import Event, Calendar
from .scraper import get_offers

IN_GAME_CONTENT = "In-Game Content"
GAMES_WITH_PRIME = "Games with Prime"

def get_url(content: dict) -> str:
	return content["externalURL"] or "https://gaming.amazon.com/home"

def create_event(offer: dict):
	event = Event()

	# Gotta remove that Z
	start_at = datetime.fromisoformat(offer["startTime"][:-1])
	end_at = datetime.fromisoformat(offer["endTime"][:-1])

	event.add('dtstart', start_at)
	event.add('dtend', end_at)
	event.add('location', get_url(offer["content"]))
	event.add('summary', offer["title"])
	event.add('description', offer["description"])
	event.add('uid', offer["id"])

	return event

def get_calendar(calendar_type: str):
	cal = Calendar()
	cal.add('prodid', '-//KAWCCO (@supersonichub1)/EN')
	cal.add('version', '2.0')
	cal.add("method", "PUBLISH")

	name = "Prime Gaming Offers"
	if calendar_type == "in_game_content":
		name += f" ({IN_GAME_CONTENT})"
	elif calendar_type == "games_with_prime":
		name += f" ({GAMES_WITH_PRIME})"

	cal.add('name', name)

	offers = get_offers()
	if calendar_type == "in_game_content":
		offers = filter(
			lambda offer: "In-Game Content" in offer["content"]["categories"],
			offers
		)
	elif calendar_type == "games_with_prime":
		offers = filter(
			lambda offer: "Games with Prime" in offer["content"]["categories"],
			offers
		)

	events = map(create_event, offers)
	for event in events:
		cal.add_component(event)

	return cal
