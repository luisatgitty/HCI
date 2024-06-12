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
        if len(self.sensors[sensor_id]) > 10:  # We need at least 10 data points to use Linear Regression
            self.analyze_data(sensor_id)

    def analyze_data(self, sensor_id):
        # Convert the data to a pandas Series
        series = pd.Series(self.sensors[sensor_id])
        
        # Define the Linear Regression model
        model = LinearRegression()

        # Fit the model
        model.fit(np.arange(len(series)).reshape(-1, 1), series.values.reshape(-1, 1))

        # Make predictions
        predictions = model.predict(np.arange(len(series), len(series)+5).reshape(-1, 1))

        # Detect anomalies: if the last data point is not within the prediction interval, it's an anomaly
        anomaly_detected = not (series.iloc[-1] >= predictions.min() and series.iloc[-1] <= predictions.max())
        if anomaly_detected:
            self.send_alert(sensor_id)

    def send_alert(self, sensor_id):
        alert = f"Alert: Potential anomaly detected in {sensor_id}"
        self.alerts.append(alert)
        print(alert)
        # Here you can add code to send an SMS alert

    def generate_report(self):
        if not self.account.logged_in:
            print("Please log in to generate a report.")
            return
        report = f"Monthly Report: {len(self.alerts)} anomalies detected this month"
        self.reports.append(report)
        print(report)
        # Here you can add code to generate a more detailed report

# Prompt the user for a username and password
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Create an account with the provided username and password
account = Account(username, password)

# Prompt the user for a username and password to login
login_username = input("Please enter your username to login: ")
login_password = input("Please enter your password to login: ")

# Try to login
account.login(login_username, login_password)

# If login is successful, prompt the user for machinery credentials
if account.logged_in:
    model = input("Please enter the model of the machinery: ")
    type = input("Please enter the type of the machinery: ")
    name = input("Please enter the name of the machinery: ")
    serial_number = input("Please enter the serial number of the machinery: ")

    # Create a machinery object with the provided credentials
    machinery = Machinery(model, type, name, serial_number)

    # Create a PredictiveTechnology object with the created account and machinery
    tech = PredictiveTechnology(account, machinery)

    # Simulate collecting data from sensors
    for i in range(1000):
        tech.collect_data(f"Sensor{i}", i % 50)  # Simulate data

    # Generate a monthly report
    tech.generate_report()

# Prompt the user to log out
logout_input = input("Do you want to log out? (yes/no): ")
if logout_input.lower() == "yes":
    account.logout()
