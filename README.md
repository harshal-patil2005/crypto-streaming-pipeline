# Real-Time Crypto Data Pipeline with Anomaly Detection 🚀

## 📌 Problem Statement

Cryptocurrency prices are highly volatile and require real-time monitoring to detect sudden spikes or drops. Traditional batch systems fail to capture these rapid changes efficiently.

This project builds a real-time data pipeline to ingest, process, and analyze crypto price data, converting it into INR and detecting anomalies using streaming techniques.

---

## 🏗️ Architecture

Crypto API → CSV (Streaming Simulation) → PySpark Structured Streaming → Window + Watermark → Anomaly Detection → Parquet Output

---

## ⚙️ Tech Stack

* PySpark
* Structured Streaming
* Python
* API Integration
* Parquet
* Git

---

## 🔄 Data Flow

1. Crypto price data is fetched from API (USD)
2. INR exchange rate is fetched from a separate API
3. Data is stored as CSV files to simulate streaming
4. PySpark reads data using Structured Streaming
5. Data is transformed and converted from USD to INR
6. Window-based aggregation is applied
7. Anomalies are detected based on price fluctuations
8. Output is stored in Parquet format with checkpointing

---

## ✨ Features

* Real-time data ingestion (simulated streaming)
* USD to INR price conversion
* Window-based aggregation
* Watermarking for late data handling
* Anomaly detection (price spikes/drops)
* Fault tolerance using checkpointing
* Optimized storage using Parquet format

---

## 📁 Project Structure

```
crypto-streaming-pipeline/
│
├── data/
│   ├── input_data/        # streaming CSV files
│   ├── output_data/       # processed results
│   ├── checkpoint/        # streaming state
│   └── inr_rate.json      # exchange rate
│
├── scripts/
│   ├── api_ingestion.py
│   ├── api_ingestion_inr.py
│
├── spark/
│   └── streaming_job.py
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run API scripts to generate data:

```
python scripts/api_ingestion.py
python scripts/api_ingestion_inr.py
```

3. Start Spark streaming job:

```
python spark/streaming_job.py
```

---

## 🧠 Key Concepts Used

* Structured Streaming
* Windowing
* Watermarking
* Checkpointing
* Data Transformation
* Real-time Processing

---

## 💬 Interview Explanation

“I built a real-time crypto data pipeline using PySpark Structured Streaming where I ingest data from APIs, simulate streaming using file-based ingestion, convert USD prices to INR, apply window-based aggregation with watermarking, and detect anomalies in price fluctuations. The processed data is stored in partitioned Parquet format with checkpointing for fault tolerance.”

---

## 🚀 Future Improvements

* Add Airflow for orchestration
* Integrate Kafka for real-time ingestion
* Add dashboard for visualization

---

## 📌 Author

Harshal Patil
