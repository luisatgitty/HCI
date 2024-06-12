from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.logged_in = True
            print("Logged in successfully! Welcome to SPTEMESRP.")
        else:
            print("Invalid username or password.")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("Logged out successfully!")
        else:
            print("You are not logged in.")

class Machinery:
    def __init__(self, model, type, name, serial_number):
        self.model = model
        self.type = type
        self.name = name
        self.serial_number = serial_number
        self.condition = 100  

    def get_status(self):  
        return f"{self.name} ({self.model}, {self.type}) is at {self.condition}% condition."

class PredictiveTechnology:
    def __init__(self, account, machinery):
        self.account = account
        self.machinery = machinery
        self.sensors = {}
        self.alerts = []
        self.reports = []

    def collect_data(self, sensor_id, data):
        if not self.account.logged_in:
            print("Please log in to collect data.")
            return
        if sensor_id not in self.sensors:
            self.sensors[sensor_id] = []
        self.sensors[sensor_id].append(data)
        if len(self.sensors[sensor_id]) > 10:  
            self.analyze_data(sensor_id)

    def generate_report(self):
        if not self.account.logged_in:
            print("Please log in to generate a report.")
            return
        report = f"Monthly Report: {len(self.alerts)} anomalies detected this month. Currently monitoring: {self.machinery.get_status()}"
        self.reports.append(report)
        print(report)

    
    def add_machinery(self):  
        add_more = input("Do you want to add more machinery to monitor? (yes/no): ")
        while add_more.lower() == "yes":
            model = input("Please enter the model of the machinery: ")
            type = input("Please enter the type of the machinery: ")
            name = input("Please enter the name of the machinery: ")
            serial_number = input("Please enter the serial number of the machinery: ")

            machinery = Machinery(model, type, name, serial_number)
            print(f"Added {machinery.name} to monitoring list.")
            print(machinery.get_status())

            add_more = input("Do you want to add more machinery to monitor? (yes/no): ")

        print("Real time machinery monitoring interface is now active.")


username = input("Please enter your username: ")
password = input("Please enter your password: ")

account = Account(username, password)


login_username = input("Please enter your username to login: ")
login_password = input("Please enter your password to login: ")


account.login(login_username, login_password)

if account.logged_in:
    model = input("Please enter the model of the machinery: ")
    type = input("Please enter the type of the machinery: ")
    name = input("Please enter the name of the machinery: ")
    serial_number = input("Please enter the serial number of the machinery: ")

    
    machinery = Machinery(model, type, name, serial_number)

   
    tech = PredictiveTechnology(account, machinery)

    
    tech.add_machinery()

    for i in range(1000):
        tech.collect_data(f"Sensor{i}", i % 50)


    tech.generate_report()

logout_input = input("Do you want to log out? (yes/no): ")
if logout_input.lower() == "yes":
    account.logout()