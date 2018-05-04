# fullcalendar-example
A simple implamentation of fullcalendar using bottle as server and mysql as database.

## How to use

### Prequests
- Python ^3.6

### Installation of packages
You will need the packages `pymysql` and `bottle`. Install it by following commands:
```bash
pip install pymysql
```
```bash
pip install bottle
```

### Database
Set up a mysql-databas and name it `fullcalendar`. Import the database in `db/fullcalendar.sql`.

Enter your database credentials in `calendar.py`

### Run the application
```bash
python bottle_app.py
```

