from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
from rich import print

# Kafka configuration
KAFKA_BROKERS = ['127.0.0.1:9092']  # Update with Kafka broker IP
TOPIC_NAME = 'my-topic-test'
CONSUMER_GROUP = 'mongo-consumer-group'

# Load API keys from secret.txt
with open('secret.txt') as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split(' = ')
            if key == 'MONGO_URI':
                MONGO_URI = value.strip("'")

# MongoDB Atlas configuration
DB_NAME = 'kafka_data'
COLLECTION_NAME = 'tweets'

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Create a Kafka consumer
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKERS,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=CONSUMER_GROUP,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("[bold green]Connected to Kafka and MongoDB Atlas. Waiting for messages...[/bold green]")

# Process incoming messages
try:
    for message in consumer:
        tweet = message.value
        print(f"[bold blue]Received tweet:[/bold blue] {tweet}")

        # Insert tweet into MongoDB Atlas
        collection.insert_one(tweet)
        print("[bold yellow]Tweet stored in MongoDB Atlas.[/bold yellow]")

except KeyboardInterrupt:
    print("[bold red]Consumer interrupted by user.[/bold red]")
finally:
    consumer.close()
    print("[bold yellow]Kafka consumer closed.[/bold yellow]")
