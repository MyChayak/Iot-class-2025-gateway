import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "172.16.2.117"
PORT = 1883
STUDENT_ID = "68123456789"  # Example student ID (not used when wildcard is applied)

# 🔹 Subscribe to temperature data from ALL student IDs
# Using '+' wildcard to match exactly one level of the topic hierarchy
TOPICS = [
    (f"", 2),  # Subscribe with QoS=2
]

def timestamp():
    """Return the current time formatted as HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")

# Callback triggered when the client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"[{timestamp()}] Connected with result code {rc}")
    # Subscribe to all topics in the TOPICS list
    for topic, qos in TOPICS:
        client.subscribe(topic, qos=qos)
        print(f"[{timestamp()}] SUBSCRIBED to {topic} with QoS={qos}")

# Callback triggered when a message is received from the broker
def on_message(client, userdata, msg):
    # Extract the last part of the topic (e.g. "temperature")
    sensor = msg.topic.split("/")[-1]
    print(f"[{timestamp()}] RECEIVED | {sensor}: {msg.payload.decode()} | QoS={msg.qos}")

# Callback for logging/debugging MQTT client activity
def on_log(client, userdata, level, buf):
    print(f"[{timestamp()}] DEBUG | {buf}")

# Create MQTT client and assign callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log  # Enable debug logging

# Connect to broker and start listening
client.connect(BROKER, PORT, 60)
client.loop_forever()
