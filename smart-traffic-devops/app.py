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

    # Metric 1: Vehicle count per location/signal/level
    vehicle_gauge = Gauge(
        'traffic_vehicle_count',
        'Number of vehicles at a location',
        ['location', 'signal', 'level'],
        registry=registry
    )

    # Metric 2: Total vehicle count
    total_vehicles = Gauge(
        'traffic_total_vehicles',
        'Total vehicle count across all signals',
        registry=registry
    )

    # Metric 3: Active signal color
    signal_gauge = Gauge(
        'traffic_signal_state',
        'Signal state (1 = active, 0 = inactive)',
        ['signal'],
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

    # Set metric values
    vehicle_gauge.labels(location=location, signal=signal, level=level).set(vehicles)
    total_vehicles.set(vehicles)

    for sig in signals:
        signal_gauge.labels(signal=sig).set(1 if sig == signal else 0)

    return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
