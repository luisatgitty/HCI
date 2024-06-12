class MentalBenderMonitor:
    def __init__(self):
        self.sensors = {}
        self.alerts = []
        self.reports = []

    def collect_data(self, sensor_id, data):
        self.sensors[sensor_id] = data
        self.analyze_data(sensor_id)

    def analyze_data(self, sensor_id):
        data = self.sensors[sensor_id]
        # Simulate an anomaly detection
        anomaly_detected = sensor_id == "Sensor500"
        if anomaly_detected:
            self.send_alert(sensor_id)

    def send_alert(self, sensor_id):
        alert = f"Alert: Potential anomaly detected in {sensor_id}"
        self.alerts.append(alert)
        print(alert)
        # Here you can add code to send an SMS alert

    def generate_report(self):
        report = f"Monthly Report: {len(self.alerts)} anomalies detected this month"
        self.reports.append(report)
        print(report)
        # Here you can add code to generate a more detailed report

# Create a MentalBenderMonitor object
monitor = MentalBenderMonitor()

# Simulate collecting data from sensors
for i in range(1000):
    monitor.collect_data(f"Sensor{i}", "Data")

# Generate a monthly report
monitor.generate_report()
