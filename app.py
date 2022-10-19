from flask import Flask, render_template, request
import mysql
from flask_mysqldb import MySQL
import mysql.connector  # or from mysql
from mysql import connector
import yaml
from operator import truediv
import time, sys
import datetime

app = Flask(__name__)

# db conf
db = yaml.load(open("db.yaml"), Loader=yaml.Loader)

app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_PASSWORD"] = db["mysql_password"]
app.config["MYSQL_DB"] = db["mysql_db"]

mysql = MySQL(app)


@app.route("/")
def create():
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO tbl_restaurant (city, street) VALUES (%s, %s)"
    val = ("test", "teststr")
    cursor.execute(sql, val)

    # cursor.execute(''' INSERT INTO tbl_terminal VALUES(restaurant_id)''')
    print(cursor)
    mysql.connection.commit()
    cursor.close()
    return "<p>Hello, World!</p>"


@app.route("/menu1")
def read1():
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu"
    cursor.execute(sql)
    result = cursor.fetchall()

    for x in result:
        print(x[2])

    return render_template("dashboard.html", result=result)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/menu_pizza")
def read_pizza():
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu"
    cursor.execute(sql)
    result = cursor.fetchall()

    for x in result:
        print(x[2])

    return render_template("menu_pizza.html", result=result)
