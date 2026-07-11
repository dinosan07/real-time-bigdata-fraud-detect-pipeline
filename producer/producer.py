import json
import time
import random
import logging
from kafka import KafkaProducer

# -----------------------------
# Logging Configuration
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Kafka Configuration
# -----------------------------
KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "transactions"
# -----------------------------
# Create Kafka Producer
# -----------------------------
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    retries=5
)

def generate_transaction():
    """
    Simulates realistic banking transaction behavior
    """

    user_id = random.randint(1, 1000)

    # 90% normal transactions
    if random.random() < 0.9:
        amount = round(random.uniform(100, 3000), 2)
    else:
        # 10% high-risk abnormal transaction
        amount = round(random.uniform(8000, 15000), 2)

    return {
        "transaction_id": random.randint(100000, 999999),
        "user_id": user_id,
        "amount": amount,
        "timestamp": time.time()
    }

# -----------------------------
# Main Loop
# -----------------------------
if __name__ == "__main__":
    logging.info("Starting Kafka Producer...")

    try:
        while True:
            transaction = generate_transaction()

            producer.send(TOPIC_NAME, transaction)
            logging.info(f"Sent: {transaction}")

            time.sleep(2)

    except KeyboardInterrupt:
        logging.info("Producer stopped manually.")

    finally:
        producer.flush()
        producer.close()
        logging.info("Kafka Producer closed.")

