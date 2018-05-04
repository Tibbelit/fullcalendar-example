import pymysql

DB_HOST = "localhost"
DB_USERNAME = "root"
DB_PASSWORD = ""
DB_NAME = "fullcalendar"

def get_events():
    '''Fetch all calendar events'''
    db = pymysql.connect(DB_HOST,DB_USERNAME, DB_PASSWORD, DB_NAME, cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM events ORDER BY id DESC")
    events = cursor.fetchall()
    db.close()
    return events

def create_event(title, start, end):
    '''Create a calendar event'''
    db = pymysql.connect(DB_HOST,DB_USERNAME, DB_PASSWORD, DB_NAME, cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("INSERT into events (title, start, end) VALUES ('{}', '{}', '{}')".format(title, start, end))
    db.commit()
    db.close()
    return {"start": start, "end": end, "title": title}
