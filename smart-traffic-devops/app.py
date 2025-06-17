from flask import Flask, jsonify, Response
import random
from datetime import datetime
from prometheus_client import CollectorRegistry, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

locations = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"]
signals = ["Red", "Yellow", "Green"]

@app.route('/')
def traffic_status():
    vehicles = random.randint(0, 100)
    signal = random.choice(signals)
    location = random.choice(locations)

    if vehicles > 70:
        level = "High"
    elif vehicles > 30:
        level = "Moderate"
    else:
        level = "Low"

    data = {
        "data": {
            "signal": signal,
            "vehicles": vehicles,
            "traffic_level": level,
            "location": location,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "status": "Traffic system live"
    }
    return jsonify(data)

@app.route('/metrics')
def metrics():
    registry = CollectorRegistry()
    traffic_gauge = Gauge(
        'traffic_vehicle_count',
        'Vehicle count at traffic signal',
        ['location', 'signal', 'level'],
        registry=registry
    )

    vehicles = random.randint(0, 100)
    signal = random.choice(signals)
    location = random.choice(locations)

    if vehicles > 70:
        level = "High"
    elif vehicles > 30:
        level = "Moderate"
    else:
        level = "Low"

    # Set metric value with custom labels
    traffic_gauge.labels(location=location, signal=signal, level=level).set(vehicles)

    return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

