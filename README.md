# ELK Log Monitoring Dashboard

An end-to-end log monitoring and alerting system built using the **Elastic Stack (ELK)**.  
This project ingests application logs, parses log levels, visualizes trends, and triggers alerts on ERROR spikes — all using the **free Elastic tier**.

---

## 📌 Features

- 📊 Interactive Kibana dashboard
- 📈 Logs volume over time
- 🚨 ERROR, WARNING, INFO metrics
- 🎨 Dynamic color-based indicators
- ⏱ Real-time monitoring (Last 15 minutes)
- 🔔 Alert rule for ERROR spikes
- 💯 Built fully on Elastic Free Tier

---

## 🛠 Tech Stack

- **Elasticsearch**
- **Logstash / Ingest Pipelines**
- **Kibana (Lens + Dashboards)**
- **Filebeat**
- **Linux**
- **Git & GitHub**

---

## 📂 Project Structure

```text
elk-log-monitoring/
├── ingest-pipeline/
│   └── python-logs-pipeline.json
├── screenshots/
│   └── dashboard.png
├── README.md

