"""
This module is for creating data tables in MySQL database.
"""

from peewee import *
import pymysql
import settings as s

# create mysql connection to check if schema exist on MySQL Server with pymysql
conn = pymysql.connect(host=s.HOST, user=s.USER, password=s.PASSWORD)

# check if database exist
exist = conn.cursor().execute("SHOW DATABASES LIKE '{}';".format(s.SCHEMA))

if not exist:
    conn.cursor().execute("CREATE DATABASE {}".format(s.SCHEMA))
    conn.close()

# Create a MySQL database connector object for Peewee ORM
mysql_db = MySQLDatabase(database=s.SCHEMA, user=s.USER, password=s.PASSWORD, host=s.HOST, port=s.PORT)


class Car(Model):
    """Define Car model for MySQL Database"""
    brand = CharField(max_length=255, null=False)
    model = CharField(max_length=255, null=False)
    year = SmallIntegerField(null=False)
    ext_color = CharField(max_length=125, null=False)
    int_color = CharField(max_length=125, null=False)
    transmission = CharField(max_length=125, null=False)
    price = DecimalField(null=False, decimal_places=3)
    phone = CharField(max_length=20, null=False)

    class Meta:
        database = mysql_db  # This model uses the "people.db" database.


# create table in the database
mysql_db.connect()
mysql_db.create_tables([Car])
mysql_db.close()
