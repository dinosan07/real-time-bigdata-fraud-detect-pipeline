from kafka import KafkaConsumer
import json
import psycopg2

# Connect to Postgres
conn = psycopg2.connect(
    host="localhost",
    database="fraud_db",
    user="admin",
    password="admin"
)
cursor = conn.cursor()

# Connect to Kafka
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started...")

for message in consumer:
    data = message.value
    
    transaction_id = data.get("transaction_id")
    user_id = data.get("user_id")
    amount = data.get("amount")
    prediction = data.get("prediction", 0)

    cursor.execute(
        """
        INSERT INTO transactions (transaction_id, user_id, amount, prediction)
        VALUES (%s, %s, %s, %s)
        """,
        (transaction_id, user_id, amount, prediction)
    )

    conn.commit()
    print("Inserted:", data)
