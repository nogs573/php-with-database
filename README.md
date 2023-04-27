# PHP-With-DB

Just messing around with PHP, a local Apache server, and MySQL database integration
using the same data from my DnD SQLite project in my [showcase repo](https://github.com/nogs573/showcase).

I converted the .db file containing the database schema for that project to a
.sql file and had to make a few manual edits to handle the same data. I can
easily set up a database with this schema using MySQL at the command line, then
insert the data contained in .csv files using a Python script with the pandas module.

If MySQL is installed, these commands can get the database with data up and running on linux.

1. `systemctl start mysql` (if the mysql service is not already running)
2. Enter MySQL monitor: `mysql -u [user] -p`
3. ```sql create database dnd;```
4. `exit;`
5. `mysql -u [user] -p dnd < DnD.sql`
6. `python3 ./insertData.py`

Next time you enter MySQL monitor, all the tables with data can be accessed.

