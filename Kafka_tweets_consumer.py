from kafka import KafkaConsumer
from json import loads
from rich import print

# Update the Kafka broker IP and port
KAFKA_BROKER = '127.0.0.1:9092'  # Replace with your Kafka broker's address
TOPIC_NAME = 'my-topic-test'         # Kafka topic to consume messages from

# Create a Kafka consumer
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=[KAFKA_BROKER],  # Connect to the Kafka broker
    auto_offset_reset='earliest',     # Start from the earliest message if no offset is committed
    enable_auto_commit=True,          # Automatically commit offsets
    group_id='my-consumer-group',     # Consumer group ID for tracking offsets
    value_deserializer=lambda x: loads(x.decode('utf-8'))  # Deserialize JSON messages
)

# Process incoming messages
print("[bold green]Connected to Kafka broker and consuming messages...[/bold green]")

try:
    for message in consumer:
        # Get the value of the message
        tweet = message.value
        # Print the message
        print(f"[bold blue]Received message:[/bold blue] {tweet}")
except KeyboardInterrupt:
    print("[bold red]Consumer stopped.[/bold red]")
finally:
    consumer.close()
    print("[bold yellow]Kafka consumer closed.[/bold yellow]")
