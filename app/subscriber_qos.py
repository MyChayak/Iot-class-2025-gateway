import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "172.16.2.117"
PORT = 1883
STUDENT_ID = 68123456789
TOPIC = f"test/qos/{STUDENT_ID}"

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

# Callback เมื่อเชื่อมต่อ broker สำเร็จ
def on_connect(client, userdata, flags, rc):
    print(f"[{timestamp()}] Connected with result code {rc}")
    client.subscribe(TOPIC, qos=2)  # subscribe ด้วย QoS สูงสุด

# Callback เมื่อรับข้อความจาก broker
def on_message(client, userdata, msg):
    print(f"[{timestamp()}] RECEIVED | QoS={msg.qos} | Topic={msg.topic} | Message={msg.payload.decode()} | msgid={getattr(msg, 'mid', 'N/A')}")

# Callback สำหรับ log debug
def on_log(client, userdata, level, buf):
    print(f"[{timestamp()}] DEBUG | {buf}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log  # เปิด debug log

client.connect(BROKER, PORT, 60)
client.loop_forever()
