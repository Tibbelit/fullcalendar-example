from bottle import route, run, template, request
import json
import calendar

@route('/')
def index():
    return template('index')

@route('/events')
def events():
    events = calendar.get_events()
    return json.dumps(events)

@route('/save-event', method="POST")
def events():
    title = request.forms.get("title")
    start = request.forms.get("start")
    end = request.forms.get("end")
    event = calendar.create_event(title, start, end)
    return json.dumps(event)


run(host='localhost', port=8080, reloader=True)
