# 🚦 Smart Traffic Monitoring & Alert System

A real-time traffic monitoring and alerting system built with **Flask**, **Prometheus**, **Grafana**, and fully deployed using **Docker** and **Kubernetes (k3s)** on an AWS EC2 instance. This project demonstrates a complete DevOps pipeline including observability, alerting, and container orchestration.

---

## 🔧 Tech Stack

| Category        | Tools Used                                  |
|----------------|----------------------------------------------|
| Language        | Python (Flask)                              |
| Containerization| Docker, Docker Compose                      |
| Orchestration   | Kubernetes (k3s)                             |
| Monitoring      | Prometheus, Grafana                         |
| Alerting        | Prometheus Alert Rules                      |
| CI/CD (optional)| Jenkins / GitHub Actions (not included yet) |
| Hosting         | AWS EC2 (Ubuntu)                            |
| GitHub          | [View Repo](https://github.com/Priyanshutripathi555/smart-traffic-devops) |

---

## 📈 Live Monitoring Dashboard

![Grafana Screenshot](https://raw.githubusercontent.com/yourusername/smart-traffic-devops/main/docs/grafana-sample.png)

---

## 📂 Project Structure

```
smart-traffic-devops/
├── app.py                      # Flask App
├── dockerfile                  # Flask Docker Image
├── requirements.txt            # Python dependencies
├── prometheus.yml              # Prometheus config
├── alert.rules.yml             # Prometheus alert rules
├── docker-compose.yml          # Docker multi-container setup
├── grafana/
│   └── traffic_dashboard.json  # Grafana dashboard config
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── prometheus-deploy.yaml
│   ├── prometheus-service.yaml
│   ├── grafana-deploy.yaml
│   └── grafana-service.yaml
```

---

## 🚀 How to Run

### 🐳 Run via Docker Compose

```bash
docker-compose up -d
```

Access:
- Flask App: http://localhost:5000/
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin/admin)

---

### ☸️ Run on Kubernetes (k3s)

1. Apply app and services:

```bash
kubectl apply -f k8s/
```

2. Create ConfigMap:

```bash
kubectl create configmap prometheus-config   --from-file=prometheus.yml   --from-file=alert.rules.yml
```

3. Restart Prometheus:

```bash
kubectl rollout restart deployment prometheus-deployment
```

4. Access on EC2:

| Component     | Port   |
|---------------|--------|
| Flask API     | `32387` |
| Prometheus    | `30090` |
| Grafana       | `31300` |

---

## 📊 PromQL Queries Used in Grafana

- **Total Vehicles:** `traffic_total_vehicles`
- **By Location:** `sum by(location) (traffic_vehicle_count)`
- **By Signal Color:** `sum by(signal) (traffic_vehicle_count)`
- **High Traffic Count:** `count(traffic_vehicle_count > 70)`
- **Active Signals:** `traffic_signal_state`
- **All Metrics Table:** `traffic_vehicle_count`

---

## 🚨 Alert Rules (Prometheus)

```yaml
- alert: HighTrafficDetected
  expr: traffic_vehicle_count > 70
  for: 10s
  labels:
    severity: warning
  annotations:
    summary: "High traffic detected"
    description: "Vehicle count exceeds threshold."
```

---

## 📌 Future Improvements

- Jenkins CI/CD Pipeline
- GitHub Actions for Auto-Deployment
- AlertManager integration (email/Slack)
- MongoDB backend for historical analytics
- Real-time camera integration for signal triggers

---

## 🤝 Author

**Priyanshu Tripathi**  
DevOps Enthusiast | TCS | AWS + Kubernetes Practitioner  
[GitHub](https://github.com/Priyanshutripathi555)

---

## 📜 License

MIT License — feel free to fork and modify this project for educational or professional use.

