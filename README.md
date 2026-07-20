# 🚀 Real-Time Big Data Pipeline for Fraud Detection

A scalable real-time fraud detection system built using Apache Kafka, Apache Spark, Machine Learning, and PostgreSQL. This project demonstrates how streaming transaction data can be processed in real time, analyzed using a trained machine learning model, and stored for further analysis.

---

## 📌 Project Overview

This project simulates a real-world financial transaction pipeline where transaction data is continuously streamed through Apache Kafka, processed using Apache Spark, classified by a machine learning model, and stored in PostgreSQL.

The system is designed to identify fraudulent transactions with low latency while maintaining scalability for high-volume data streams.

---

## 🏗️ Architecture

```
Transaction Generator
        │
        ▼
Apache Kafka (Producer)
        │
        ▼
Apache Spark Streaming
        │
        ▼
ML Fraud Detection Model
        │
        ▼
PostgreSQL Database
        │
        ▼
Analytics & Dashboard
```

---

## 🛠️ Technologies Used

- Python 3.x
- Apache Kafka
- Apache Spark
- PySpark
- PostgreSQL
- Scikit-learn
- Pandas
- Joblib
- Docker
- Linux (Ubuntu / WSL)

---

## 📂 Project Structure

```
real-time-bigdata-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── fraud_model.pkl
│
├── producer/
│   └── kafka_producer.py
│
├── consumer/
│   └── spark_consumer.py
│
├── scripts/
│   └── pipeline.py
│
├── database/
│   └── create_tables.sql
│
├── notebooks/
│
├── requirements.txt
│
├── docker-compose.yml
│
└── README.md
```

---

## ⚙️ Features

- Real-time transaction streaming
- Kafka Producer & Consumer
- Apache Spark Structured Streaming
- Machine Learning-based fraud prediction
- PostgreSQL data storage
- Scalable streaming architecture
- Docker support
- Easy deployment

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/real-time-bigdata-pipeline.git

cd real-time-bigdata-pipeline
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Start Kafka & Zookeeper

```bash
docker-compose up -d
```

or manually

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties
```

---

## ▶️ Run Kafka Producer

```bash
python producer/kafka_producer.py
```

---

## ▶️ Run Spark Consumer

```bash
spark-submit consumer/spark_consumer.py
```

---

## 🗄️ Database

Create PostgreSQL database.

```sql
CREATE DATABASE fraud_detection;
```

Run

```sql
database/create_tables.sql
```

---

## 🤖 Machine Learning Model

The fraud detection model is trained using Scikit-learn and saved as:

```
models/fraud_model.pkl
```

The Spark Consumer loads this model and predicts whether incoming transactions are fraudulent.

---

## 📊 Sample Workflow

1. Producer generates transaction records.
2. Kafka streams the data.
3. Spark consumes the stream.
4. ML model predicts fraud.
5. Results are stored in PostgreSQL.
6. Dashboard can visualize the stored data.

---

## 📈 Future Improvements

- Apache Airflow integration
- Grafana dashboard
- Prometheus monitoring
- AWS deployment
- Kubernetes orchestration
- Real-time alert notifications
- Streamlit dashboard

---

## 👨‍💻 Author

**S. Anbumathi**

B.Tech Artificial Intelligence & Data Science

The Kavery Engineering College

GitHub: https://github.com/dinosan

LinkedIn: https://www.linkedin.com/in/anbu-mathi-2528162a3/

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

---

## 📜 License

This project is licensed under the MIT License.
