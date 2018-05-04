import pymysql

def get_events():
    '''Hämtar alla events från databasen'''
    # Anslut till databasen
    db = pymysql.connect("localhost","root","","fullcalendar", cursorclass=pymysql.cursors.DictCursor)
    # Skapa en pekare till databasen
    cursor = db.cursor()
    # Skicka frågan till databasen
    cursor.execute("SELECT * FROM events ORDER BY id DESC")
    # Spara events i en variabel
    events = cursor.fetchall()
    # Stäng databasanslutningen
    db.close()
    return events

def save_event(title, start, end):
    '''Spara ett nytt event i databasen'''
    # Anslut till databasen
    db = pymysql.connect("localhost","root","","fullcalendar", cursorclass=pymysql.cursors.DictCursor)
    # Skapa en pekare till databasen
    cursor = db.cursor()
    # Skicka frågan till databasen
    cursor.execute("INSERT into events (title, start, end) VALUES ('{}', '{}', '{}')".format(title, start, end))
    # Spara i db
    db.commit()
    # Stäng databasanslutningen
    db.close()
    return {"start": start, "end": end, "title": title}
