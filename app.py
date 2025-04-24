from flask import Flask, request, render_template_string

app = Flask(__name__)

sensor_data = {"temperature": "N/A", "humidity": "N/A"}

@app.route("/")
def home():
    return render_template_string("""
        <h1>Pico Sensor Data</h1>
        <p><strong>Temperature:</strong> {{ temp }}°C</p>
        <p><strong>Humidity:</strong> {{ hum }}%</p>
    """, temp=sensor_data["temperature"], hum=sensor_data["humidity"])

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    sensor_data["temperature"] = data.get("temperature", "N/A")
    sensor_data["humidity"] = data.get("humidity", "N/A")
    return "OK"
