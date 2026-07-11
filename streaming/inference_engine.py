import os
import json
import joblib
import logging
import psycopg2
from kafka import KafkaConsumer

# -----------------------------
# Logging Configuration
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Configuration
# -----------------------------
KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "transactions"

DB_HOST = "localhost"
DB_NAME = "fraud_db"
DB_USER = "admin"
DB_PASSWORD = "admin"

MODEL_PATH = BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "fraud_model.pkl")


# -----------------------------
# Load ML Model (Loaded Once)
# -----------------------------
model = joblib.load(MODEL_PATH)
logging.info("Model loaded successfully.")

# -----------------------------
# Kafka Consumer
# -----------------------------
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="latest",
    enable_auto_commit=True
)

logging.info("Kafka Consumer started...")

# -----------------------------
# PostgreSQL Connection
# -----------------------------
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cursor = conn.cursor()

# -----------------------------
# Processing Loop
# -----------------------------
for message in consumer:
    transaction = message.value

    transaction_id = transaction["transaction_id"]
    user_id = transaction["user_id"]
    amount = transaction["amount"]

    # ML Prediction
    import pandas as pd

# Custom fraud threshold
THRESHOLD = 0.6

input_df = pd.DataFrame({
    "amount": [amount]
})

probability = model.predict_proba(input_df)[0][1]

if probability > THRESHOLD:
    prediction = 1
else:
    prediction = 0


    # Insert into DB
    # Insert into transactions table
cursor.execute("""
    INSERT INTO transactions (transaction_id, user_id, amount, prediction, fraud_probability)
    VALUES (%s, %s, %s, %s, %s)
""", (transaction_id, user_id, amount, prediction, probability))

# If fraud detected, insert into alerts table
if prediction == 1:
    cursor.execute("""
        INSERT INTO fraud_alerts (transaction_id, user_id, amount, fraud_probability)
        VALUES (%s, %s, %s, %s)
    """, (transaction_id, user_id, amount, probability))

# Commit once after all operations
conn.commit()

