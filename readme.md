
````markdown
# 🧠 AI Log Insight System 🚀  
**Detect anomalies and problematic logs in real-time using Go, Python, Docker, and Kubernetes**

---

## 📘 Overview

**AI Log Insight System** is a cloud-native project designed to automatically **detect anomalies in application logs** using **machine learning**.  
It collects logs, analyzes them in real-time, and helps engineers **pinpoint unusual or problematic behavior** before it causes failures.

---

## 🧩 What Does This Project Do?

- 📝 **Collects logs** from your apps or servers (think of it as "real-time note-taking").  
- 🤖 **Analyzes logs automatically** using a machine learning model (Isolation Forest).  
- ⚠️ **Detects anomalies** — any log entries that look suspicious or abnormal.  
- 📊 **Provides easy APIs** to fetch and visualize problematic logs.  

---

## ⚙️ How It Works

| Component | Description |
|------------|-------------|
| **Go Microservice** | Receives incoming log events and stores them in Redis. |
| **Redis** | Acts as a fast data pipeline and cache between services. |
| **Python Microservice** | Uses `IsolationForest` (from scikit-learn) to detect anomalies and serves results via an API. |
| **Docker & Kubernetes** | Containerize and orchestrate both services for scalable deployments. |

---

### 🧪 Example Flow

<details>
<summary>🔍 Click to Expand Example</summary>

#### 1️⃣ Send logs to the Go service:
```bash
curl -X POST http://localhost:8080/ingest \
  -H 'Content-Type: application/json' \
  -d '{"metric":2.1,"error_rate":0.5,"latency":800}'
````

#### 2️⃣ Ask the Python service to analyze them:

```bash
curl http://localhost:5000/analyze
```

#### ✅ Example Response:

```json
[
  {
    "metric": 2.1,
    "error_rate": 0.5,
    "latency": 800,
    "anomaly": true
  }
]
```

</details>

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ai-log-insight.git
cd ai-log-insight
```

### 2️⃣ Build and Start Services

```bash
docker-compose up --build
```

This will spin up:

* A Go-based log ingestion service (port **8080**)
* A Python anomaly detection service (port **5000**)
* A Redis instance (for message sharing)

### 3️⃣ Send Logs and Analyze

```bash
# Send log to Go service
curl -X POST http://localhost:8080/ingest \
  -H 'Content-Type: application/json' \
  -d '{"metric":1.2,"error_rate":0.01,"latency":100}'

# Analyze logs using Python API
curl http://localhost:5000/analyze
```

---

## 🧠 What Problem Does This Solve?

✅ Detects **outliers in real-time logs** automatically.
✅ Saves **hours of manual searching** through large log files.
✅ Helps engineers **respond faster** to outages or attacks.
✅ Improves **system reliability** and reduces mean-time-to-detect (MTTD).

---

## ☸️ How to Deploy in Production

1. **Convert Docker Compose → Kubernetes YAML**

   * `deployment.yaml` and `service.yaml` for both Go and Python microservices.

2. **Use Cloud Redis** (e.g., AWS ElastiCache or Redis Cloud).

3. **Add Authentication** for APIs (JWT / OAuth).

4. **Integrate Alerting**

   * Connect Slack, PagerDuty, or email notifications.

5. **Monitor with Prometheus & Grafana** for metrics.

6. **Add Long-term Storage** (PostgreSQL / S3 / ElasticSearch).

7. **Enable Horizontal Scaling** for Python workers on heavy loads.

---

## 🧰 Technology Stack

| Layer                             | Technology            |
| --------------------------------- | --------------------- |
| **Backend (Log Collector)**       | Go (Golang)           |
| **ML Engine (Anomaly Detection)** | Python (scikit-learn) |
| **Message Cache**                 | Redis                 |
| **Containerization**              | Docker                |
| **Orchestration**                 | Kubernetes            |
| **ML Model**                      | IsolationForest       |
| **Data Format**                   | JSON-based log events |

---

## 📈 Architecture Overview

```text
 ┌───────────────────┐
 │   Applications     │
 │ (Emit Logs JSON)   │
 └────────┬───────────┘
          │
          ▼
 ┌────────────────────┐
 │  Go API Service     │
 │ /ingest endpoint    │
 └────────┬────────────┘
          │
          ▼
     ┌────────┐
     │ Redis  │  ← Fast log queue
     └────────┘
          │
          ▼
 ┌────────────────────┐
 │ Python ML Service  │
 │ /analyze endpoint  │
 │ IsolationForest ML │
 └────────────────────┘
```

---

## 🧩 Example Docker Compose Setup

```yaml
version: '3.8'
services:
  go-service:
    build: ./go-service
    ports:
      - "8080:8080"
    depends_on:
      - redis

  python-service:
    build: ./python-service
    ports:
      - "5000:5000"
    depends_on:
      - redis

  redis:
    image: redis:latest
    ports:
      - "6379:6379"
```

---

## 🔮 Future Enhancements

* 🧠 **Advanced AI Models** — Deep learning or LSTM-based anomaly detection
* 💬 **LLM Summaries** — Use GPT / LangChain to explain anomalies
* 📊 **Dashboard UI** — Build visualization panel for real-time anomalies
* 🔔 **Alert Integrations** — Slack, PagerDuty, or Discord webhooks
* 🌩 **Cloud Native Scaling** — Deploy to AWS/GCP/Azure clusters

---

## 🧪 Example Anomaly Detection (Python)

```python
from sklearn.ensemble import IsolationForest
import numpy as np

data = np.array([[1.2, 0.01, 100], [2.1, 0.5, 800], [1.3, 0.02, 120]])
model = IsolationForest(contamination=0.1)
labels = model.fit_predict(data)
print(labels)  # [-1 indicates anomaly]
```

---

## 👨‍💻 Author

**Sorabh Lahoti**
🚀 Full-Stack Developer | Ex-RBM Software | NIT Rourkela

* GitHub: [@sorabhlahoti](https://github.com/sorabhlahoti)
* LinkedIn: [Sorabh Lahoti](https://www.linkedin.com/in/sorabh-lahoti-b510b6211/)
* Email: **[sorabhlahoti07@gmail.com](mailto:sorabhlahoti07@gmail.com)**

---

## 📝 License

This project is licensed under the **MIT License** — free to use and modify.

---

## ⭐ Contribute

If you find this project useful, please **star the repo**, **open issues**, or **submit pull requests**.
Contributions are welcome!

---

### 🧭 Summary

| Key Feature          | Description                                |
| -------------------- | ------------------------------------------ |
| **Language**         | Go + Python                                |
| **Machine Learning** | IsolationForest                            |
| **Infrastructure**   | Docker + Kubernetes                        |
| **Storage**          | Redis                                      |
| **Goal**             | Real-time anomaly detection in system logs |

---

**🚀 Smart logging meets AI — empowering DevOps with real-time anomaly detection.**

