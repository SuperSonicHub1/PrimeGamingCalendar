from flask import Blueprint, Response, render_template
from .calendar import get_calendar

views = Blueprint("views", __name__, url_prefix="/")

@views.route('/')
def index():
  return render_template("index.html")

@views.route('/calendar.ics')
def cal():
	cal = get_calendar("all")
	return Response(response=cal.to_ical(), mimetype="text/calendar")

@views.route('/in_game_content.ics')
def in_game_content_cal():
	cal = get_calendar("in_game_content")
	return Response(response=cal.to_ical(), mimetype="text/calendar")

@views.route('/games_with_prime.ics')
def games_with_prime_cal():
	cal = get_calendar("games_with_prime")
	return Response(response=cal.to_ical(), mimetype="text/calendar")
