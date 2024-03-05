# Mario and Luigi's Pizzeria

This is a collaborative project for which we were given a prompt and an interview transcript about a family business. We had to define the problem statement and build an IT solution that would improve the current situation of the business. Our solution consists of an interactive and easy to use order interface for the customers to use when ordering, separate GUIs for the chef and cashier to see the current status of the orders and an embedded system for a smart oven that would send real-time information to the employees.
<br/><br/>Team size: 3 people, Project duration: 3 weeks, Position: Team Leader

## Features
* Online menu designed for built-in tablets for customers
* Online ordering process and cart functionality
* Order overview before checkout
* Smart oven activated from the chef's GUI that keeps track of cooking time and sends back real-time information
* Database for persistance

## Programming Languages

* HTML5, CSS3 and JavaScript for building the web pages
* Python for setting up the Arduino Uno as a smart oven
* SQL for creating a script for database initialization

## Prerequisites
First install all libraries from the requirements.txt file
```
pip install -r requirements.txt
```
Then activate the virtual environment for python
```
.\venv\Scripts\activate
```
Lastly run the application
```
flask run
```
<br/>
Create a phpMyAdmin database and run the sql file in order to populate the app with data for the menu
<br/><br/>
Connect an Arduino One to your computer

## Executing program
Open two terminals (one for the arduino setup and one for the website) and run both at the same time
