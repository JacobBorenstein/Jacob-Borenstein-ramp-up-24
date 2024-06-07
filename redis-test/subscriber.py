import redis

r = redis.Redis(host='localhost', port=6379)

pubsub = r.pubsub()
pubsub.subscribe('channel')

print("Subscriber is listening...")

for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Received message: {message['data'].decode('utf-8')}")