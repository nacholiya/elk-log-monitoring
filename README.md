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
├── alerts/
│   └── error-spike-rule.json
├── filebeat/
│   └── filebeat.yml
├── ingest-pipeline/
│   └── python-logs-pipeline.json
├── kibana/
│   └── dashboards.ndjson
├── python-app/
│   ├── app.py
│   └── requirements.txt
├── screenshots/
│   └── dashboard.png
└── README.md


---

## 📥 Import Kibana Dashboard & Alerts

### Import Dashboard
1. Open **Kibana**
2. Go to **Stack Management → Saved Objects**
3. Click **Import**
4. Select `kibana/dashboards.ndjson`
5. Confirm import

---

### Restore Alert Rule
1. Go to **Stack Management → Rules**
2. Click **Create rule**
3. Choose **Index threshold**
4. Recreate the rule using `alerts/error-spike-rule.json`
