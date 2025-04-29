# Real-Time Product Review Sentiment Analysis Pipeline Using AWS

This project demonstrates a scalable, end-to-end **real-time sentiment analysis pipeline** using **AWS services**, built to process, classify, and visualize customer product reviews. It simulates live data ingestion using Kinesis, stores raw data in S3, performs batch sentiment analysis using EMR + PySpark, and pushes classified results into DynamoDB, with interactive dashboards powered by Power BI.

---

## 🧩 Tech Stack

**AWS Services Used:**
- Amazon EC2
- Amazon Kinesis Data Streams
- AWS Lambda
- Amazon S3
- Amazon EMR (PySpark)
- Amazon DynamoDB
- Power BI

**Languages & Tools:**
- Python, PySpark, Boto3
- Power BI Desktop

---

## 🚀 Key Features

- Real-time ingestion of simulated reviews using EC2 + Kinesis
- Serverless transformation using AWS Lambda to store raw data in S3
- Batch sentiment analysis using PySpark on Amazon EMR
- Storage of processed results in DynamoDB for fast querying
- Interactive dashboards created with Power BI

---

## 🔄 Data Flow Architecture

```
[EC2: review_producer.py]
     ↓
[Kinesis Stream]
     ↓
[AWS Lambda → raw-reviews/ in S3]
     ↓
[Amazon EMR (PySpark) → sentiment_analysis.py]
     ↓
[Processed reviews to S3: processed-reviews/]
     ↓
[Python script → DynamoDB (processed_reviews)]
     ↓
[Power BI Dashboard from DynamoDB or JSON]
```

---

## 📂 Project Structure

```
aws-sentiment-pipeline/
├── scripts/
│   ├── review_producer.py             # EC2 review generator
│   ├── lambda_to_s3.py                # Lambda function for Kinesis → S3
│   ├── sentiment_analysis.py          # EMR PySpark script
│   └── upload_to_dynamodb.py          # Script to push to DynamoDB
│
├── sample_data/
│   └── example_review_batch.json      # Sample JSON
│
├── architecture/
│   └── aws_sentiment_pipeline.png     # Architecture diagram
│
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
└── LICENSE                            # (optional)
```

---

## 📊 Sample Output (Processed Review)

```json
{
  "review_id": "b7a98b13-4a9c-4cd0-8dd6-39e8f27fd7ea",
  "review": "Exceeded my expectations!",
  "sentiment": "Positive"
}
```

---

## 📊 Dashboard (Power BI)

Visuals include:
- Sentiment breakdown (Positive/Negative/Neutral)
- Word cloud of review terms
- Table view with filters by sentiment
- Time trend (optional if timestamp is added)

---

## 🔧 Setup & Deployment

### 1. Run `review_producer.py` from EC2
### 2. Deploy `lambda_to_s3.py` to AWS Lambda (trigger: Kinesis)
### 3. Launch EMR cluster and submit `sentiment_analysis.py`
### 4. Run `upload_to_dynamodb.py` to populate DynamoDB
### 5. Connect Power BI to S3/JSON or DynamoDB to build dashboard



