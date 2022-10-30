from itertools import count, product
import random
from re import A
from xml.etree.ElementTree import tostring
from flask import Flask, render_template, request, redirect
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


shopCart = []
orderSummary = []


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


@app.route("/home")
def home():
    return render_template("home.html")

#MENUS
#pizza
@app.route("/menu_pizza")
def read_pizza():
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu WHERE type = 'pizza'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return render_template("menu_pizza.html", result=result)

    
@app.route("/menu_pizza/<int:id>")
def read_pizza_handle(id):
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu WHERE type = 'pizza'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    shopCart.append(id)
    print(shopCart)

    return render_template("menu_pizza.html", result=result)

#pasta
@app.route("/menu_pasta")
def read_pasta():
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu WHERE type = 'pasta'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return render_template("menu_pasta.html", result=result)

    
@app.route("/menu_pasta/<int:id>")
def read_pasta_handle(id):
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu WHERE type = 'pasta'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    shopCart.append(id)
    print(shopCart)

    return render_template("menu_pasta.html", result=result)

#desserts
@app.route("/menu_desserts")
def read_dessert():
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu WHERE type = 'dessert'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return render_template("menu_desserts.html", result=result)

    
@app.route("/menu_desserts/<int:id>")
def read_dessert_handle(id):
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu WHERE type = 'dessert'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    shopCart.append(id)
    print(shopCart)

    return render_template("menu_desserts.html", result=result)

#drink
@app.route("/menu_drinks")
def read_drinks():
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu WHERE type = 'drinks'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return render_template("menu_drinks.html", result=result)

    
@app.route("/menu_drinks/<int:id>")
def read_drinks_handle(id):
    cursor = mysql.connection.cursor()
    sql = "select * from tbl_menu WHERE type = 'drinks'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    shopCart.append(id)
    print(shopCart)

    return render_template("menu_drinks.html", result=result)




# ORDER DETAILS
@app.route("/order_details")
def order_details():
    orderList = []
    result = []
    for x in shopCart:
        a = str(x)
        sql = "SELECT tbl_menu.name, tbl_menu.price, tbl_menu.menu_id FROM tbl_menu WHERE tbl_menu.menu_id =" + a
        cursor = mysql.connection.cursor()
        # sql = "SELECT tbl_orderrow.row_id, tbl_orderrow.quantity, tbl_menu.name, tbl_menu.price FROM tbl_orderrow INNER JOIN tbl_menu ON tbl_orderrow.menu_id = tbl_menu.menu_id WHERE tbl_orderrow.order_id = 4"
        cursor.execute(sql)
        result = cursor.fetchall()
        orderList.append(result)
        
    print(orderList)
    
    for x in orderList:
        order = []
        count = 0
        count = orderList.count(x)
        order.append(x[0])
        order.append(count)
        if order not in orderSummary:
            orderSummary.append(order)
        
    print("ordersummary:")        
    print(orderSummary)
    
    
    return render_template("order_details.html", result=orderSummary)

@app.route("/order_details/<int:id>")
def order_details_handler(id):
 #remove
    i = 0
    indexList = []
    for x in orderSummary:
        if x[0][2] == id:
            x[1] -= 1
            if x[1] == 0:
                indexList.append(i)
            break
        i += 1
    print(indexList)
    for x in indexList:  
        orderSummary.pop(x)
                
    return render_template("order_details.html", result=orderSummary)


#SUBMIT ORDER 
@app.route("/submit_order")
def submit_order():    
   
    global orderTrack
    orderTrack = []
   
   #generate order number 
    def listToString(s):  
        str1 = ""
        for ele in s:
            str1 += ele
        return str1
    
    a = str(random.randint(0, 9))
    b = str(random.randint(0, 9))
    c = str(random.randint(0, 9))
    abc = [a, b, c]
    
    orderNumber = listToString(abc)
    orderTrack.append(orderNumber)
    
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO tbl_order (`order_nr`, `terminal_id`) VALUES (%s, %s)"
    val = (orderNumber, 1)
    cursor.execute(sql, val)
    
    #ID OF ORDER CREATED
    orderId = cursor.lastrowid
    orderTrack.append(orderId)
    
    # cursor.execute(''' INSERT INTO tbl_terminal VALUES(restaurant_id)''')
    print(cursor)
    mysql.connection.commit()
    cursor.close()
    
    for x in orderSummary:
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO tbl_orderrow (`menu_id`, `order_id`, `quantity`) VALUES (%s, %s, %s)"
        val = (x[0][2], orderId, x[1])
        cursor.execute(sql, val)
        print(cursor)
        mysql.connection.commit()
        cursor.close()

    # cursor.execute(''' INSERT INTO tbl_terminal VALUES(restaurant_id)''')

    
    return redirect("/track_order")


#TRACK ORDER 
@app.route("/track_order")
def track_order():    
    print(shopCart)
    print(orderSummary)
    shopCart.clear()
    orderSummary.clear()
    print(shopCart)
    print(orderSummary)
    cursor = mysql.connection.cursor()
    a = str(orderTrack[1])
    sql = "SELECT SUM(tbl_orderrow.quantity * tbl_menu.price) AS total FROM tbl_orderrow INNER JOIN tbl_menu ON tbl_orderrow.menu_id = tbl_menu.menu_id WHERE tbl_orderrow.order_id =" + a

    cursor.execute(sql)
    result = cursor.fetchall()
    
    return render_template("track_order.html", orderTrack = orderTrack, result = result)


# CASHIER PAGE
@app.route("/cashier")
def cashier():
    
    cursor = mysql.connection.cursor()
    sql = "SELECT DISTINCT order_id FROM `tbl_orderrow`"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    cashierList = []
    
    for orderId in result:
        
        order = []
        products = []
        
        a = str(orderId[0])
        cursor = mysql.connection.cursor()
        sql = "SELECT tbl_order.order_id,tbl_order.order_nr, tbl_orderrow.quantity, tbl_menu.name, tbl_menu.price * tbl_orderrow.quantity FROM `tbl_orderrow`, tbl_menu, tbl_order WHERE tbl_menu.menu_id = tbl_orderrow.menu_id AND tbl_order.order_id = tbl_orderrow.order_id AND tbl_order.order_id = " + a
        cursor.execute(sql)
        result1 = cursor.fetchall()
        
        totalPrice = 0
        for row in result1:
            totalPrice += row[4]
            
        
        for row in result1:
            productQuantityPrice = []
            if row[0] not in order:
                order.append(row[0])
                order.append(row[1])
                order.append(totalPrice)

            productQuantityPrice.append(row[2])
            productQuantityPrice.append(row[3])
            productQuantityPrice.append(row[4])
            
            products.append(productQuantityPrice)
            
        order.append(products)
        cashierList.append(order)
        
    print(cashierList)
    
    return render_template("cashier.html", resultCashier=cashierList)

@app.route("/cashier/<int:id>")
def cashier_handler(id):
 #remove
    a = str(id)
    cursor = mysql.connection.cursor()
    sql = "DELETE FROM tbl_order WHERE order_id = " + a
    cursor.execute(sql)
    mysql.connection.commit()
    cursor.close()
                
    return redirect("/cashier")

