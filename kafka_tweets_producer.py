import tweepy
from json import dumps
from kafka import KafkaProducer
from rich import print
from time import sleep

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092'],
    value_serializer=lambda K: dumps(K).encode('utf-8')
)

# Load API keys from secret.txt
with open('secret.txt') as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split(' = ')
            if key == 'BEARER_TOKEN':
                BEARER_TOKEN = value.strip("'")

# Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define the search query
query = 'music lang:en'

# Search for recent tweets
response = client.search_recent_tweets(
    query=query,
    max_results=100,  # Adjust to your desired count (max 100 per request)
    tweet_fields=['id', 'text', 'author_id', 'created_at', 'entities', 'lang'],
    user_fields=['username', 'location', 'public_metrics']
)

# Send tweets to Kafka
for tweet in response.data:
    cur_data = {
        "id_str": tweet.id,
        "username": tweet.author_id,  # To get detailed user info, use additional requests
        "tweet": tweet.text,
        "location": None,  # Requires fetching user details (not included in basic tweet object)
        "retweet_count": None,  # Not included in v2 response unless expanded
        "favorite_count": None,  # Not included in v2 response unless expanded
        "followers_count": None,  # Not included in v2 response unless expanded
        "lang": tweet.lang
    }
    producer.send('my-topic-test', value=cur_data)
    print(cur_data)
    sleep(0.5)
