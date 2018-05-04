# fullcalendar-example
A simple implamentation of fullcalendar using bottle as server and mysql as database. Using:
- [FullCalendar](https://fullcalendar.io/)
- [Bottle](http://bottlepy.org)
- [Bootstrap](http://getbootstrap.org)

## How to use

### Prequests
- Python ^3.6
- MySQL-database

You will need the packages `pymysql` and `bottle`. Install it by following commands:
```bash
pip install pymysql
```
```bash
pip install bottle
```

### Application setup
1. Clone the repository
```bash
git clone https://github.com/Tibbelit/fullcalendar-example.git
```
2. Navigate to the project folder
```bash
cd fullcalendar-example
```
3. Database setup
- Create a mysql-databas and name it `fullcalendar`. Import the database (found in `db/fullcalendar.sql`).
- Enter your database credentials in `calendar.py`

4. Run the web application
```
python bottle_app.py
```

5. Open your favorite browser and navigate to `http://localhost:8080`