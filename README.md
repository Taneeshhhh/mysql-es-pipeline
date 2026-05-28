# MySQL to Elasticsearch Pipeline

A simple ETL-style data pipeline that fetches relational data from MySQL, transforms it into JSON documents, indexes it into Elasticsearch, and visualizes it through Grafana dashboards.

---

## Architecture

```text
MySQL
   ↓
Python ETL Script
   ↓
Elasticsearch
   ↓
Grafana Dashboard
```

---

## Features

* Fetches structured relational data from MySQL
* Converts SQL rows into Elasticsearch-compatible JSON documents
* Indexes documents into Elasticsearch
* Supports fast search and aggregation queries
* Visualizes indexed data using Grafana dashboards
* Demonstrates foundational ETL and analytics pipeline concepts

---

## Tech Stack

* Python
* MySQL
* Elasticsearch
* Kibana
* Grafana

---

## Project Structure

```text
mysql-es-pipeline/
│
├── src/
│   ├── mysql_to_es.py
│   ├── config.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-url>
cd mysql-es-pipeline
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### CMD

```cmd
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Services

### Start Elasticsearch

```powershell
cd C:\elasticsearch-9.4.1\bin
.\elasticsearch.bat
```

---

### Start Kibana

```powershell
cd C:\kibana-9.4.1\bin
.\kibana.bat
```

Kibana UI:

```text
http://localhost:5601
```

---

### Start Grafana

Grafana UI:

```text
http://localhost:3000
```

---

## Running the Pipeline

```bash
python src/mysql_to_es.py
```

---

## Elasticsearch Verification

Open Kibana Dev Tools and run:

```json
GET students/_search
{
  "query": {
    "match_all": {}
  }
}
```

---

## Future Improvements

* Incremental synchronization using timestamps
* CDC (Change Data Capture)
* Kafka-based streaming pipelines
* Debezium integration
* Real-time dashboard updates
* Dockerized deployment

---

## Learning Outcomes

This project demonstrates:

* ETL pipeline fundamentals
* Python database integration
* Elasticsearch indexing and querying
* Grafana visualization workflows
* Search-oriented architecture concepts
* Relational → document-model transformation
