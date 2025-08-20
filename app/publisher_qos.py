import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "172.30.15.133"
PORT = 1883
STUDENT_ID = 68123456789
TOPIC = f"test/qos/{STUDENT_ID}/temperature"

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

# Callback สำหรับ log debug
def on_log(client, userdata, level, buf):
    print(f"[{timestamp()}] DEBUG | {buf}")

# Callback สำหรับ PUBACK (QoS 1)
def on_publish(client, userdata, mid):
    print(f"[{timestamp()}] PUBLISHED | msgid={mid}")

client = mqtt.Client()
client.on_log = on_log
client.on_publish = on_publish

client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        message = input("Enter message to publish: ")
        qos_level = int(input("Enter QoS level (0, 1, 2): "))
        result = client.publish(TOPIC, message, qos=qos_level)
        print(f"[{timestamp()}] PUBLISH REQUESTED | QoS={qos_level} | Message='{message}' | msgid={result.mid}")
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()
