from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
import json
import base64

# TODO(developer)
project_id = "michael-gilbert-dev"

def pubsub_pull(project_id):
    project_id = project_id
    topic_id = "riot-extractor"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)
    

    player = {
            "data" : {
                "user_name" : "ty6009",
                "Api" : "RGAPI-95c754a3-c2da-4960-bb68-7d61a2dd6847"
                }
        }

    # Data must be a bytestring
    data = json.dumps(player).encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

    print(f"Published messages to {topic_path}.")

subscription_id = "riot-extractor-pull"

def receiving_message(project_id, subscription_id):
    # Number of seconds the subscriber should listen for messages
    timeout = 5.0

    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_id}`
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        print(f"Received {message}.")
        message.ack()
    
    received_message = pubsub_v1.subscriber.message.Message
    event = base64.b64decode(received_message).decode('utf-8')
    decoding = json.loads(event)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")

    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.


def listening_to_pubsub(event, context):
    print(f"{json.dumps(event)}")
    decoded_data = base64.b64decode(event['data'])
    print(type(decoded_data))
    raw_json_data = json.loads(decoded_data)
    print(type(raw_json_data))

    desired_username = raw_json_data['user_name']
    desired_api = raw_json_data['Api']

    return desired_username, desired_api


pubsub_pull(project_id)
listening_to_pubsub(event, context)
