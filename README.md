# Project: Twitter to MongoDB Pipeline using Kafka

This project collects tweets from Twitter using the Twitter API, processes them with Kafka, and stores the data in MongoDB for further use. Below is an overview of the project and instructions to set it up.

---

## Project Structure

- **`kafka_tweets_producer.py`**: Connects to the Twitter API and sends tweets to a Kafka topic.
- **`kafka_tweets_consumer.py`**: Consumes tweets from Kafka and processes them.
- **`mongo_consumer.py`**: Stores the processed tweets from Kafka into MongoDB.
- **`secret.txt`**: Contains sensitive credentials such as Twitter API keys and MongoDB connection details.
- **`README.md`**: Documentation for the project.

---

## Prerequisites

Before you start, ensure the following are installed:

1. **Python 3.6+**
2. **Kafka** (Apache Kafka with Zookeeper)
3. **MongoDB** (Local or cloud instance)
4. **Twitter Developer Account** for API keys

---

## Secrets Configuration

### What is `secret.txt`?
The `secret.txt` file is used to store sensitive credentials securely. This file must be in the same directory as the project scripts.

### Add the following details to `secret.txt`:
```plaintext
BEARER_TOKEN = 'your_twitter_api_bearer_token'
MONGO_URI = 'your_mongodb_connection_uri'
```

- **`BEARER_TOKEN`**: Obtain it from your Twitter Developer Portal.
- **`MONGO_URI`**: This is your MongoDB connection string, in the format:
  ```
  mongodb://<username>:<password>@<host>:<port>/<database_name>
  ```
  Example:
  ```
  mongodb://localhost:27017/twitter_db
  ```

### Example of `secret.txt`:
```plaintext
BEARER_TOKEN = 'YOUR_TWITTER_BEARER_TOKEN'
MONGO_URI = 'mongodb://localhost:27017/twitter_db'
```

---

## How to Run

1. **Start Kafka:**
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   bin/kafka-server-start.sh config/server.properties
   ```

2. **Run the Kafka Producer:**
   This script collects tweets and sends them to a Kafka topic.
   ```bash
   python kafka_tweets_producer.py
   ```

3. **Run the Kafka Consumer:**
   This script consumes the tweets and processes them.
   ```bash
   python kafka_tweets_consumer.py
   ```

4. **Run the MongoDB Consumer:**
   This script saves the processed tweets to MongoDB.
   ```bash
   python mongo_consumer.py
   ```

---

## Key Features

- **Twitter API Integration**: Fetch tweets based on a search query or hashtag.
- **Kafka Integration**: Streams tweets in real-time using Kafka producers and consumers.
- **MongoDB Storage**: Stores processed tweets for further use or analysis.

---

## Additional Notes

- Ensure the `secret.txt` file is properly configured before running any script.
- Test the connection to Kafka and MongoDB before starting the producer and consumer scripts.
- Customize the search query in `kafka_tweets_producer.py` to collect specific types of tweets.

---

