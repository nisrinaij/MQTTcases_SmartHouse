"""
Skenario 1: Komunikasi Dasar Publisher-Subscriber
Studi Kasus: Smart Room Monitoring

Subscriber ini menerima data suhu ruangan dari topik:
rumah/kamar_tidur/suhu
"""

import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "rumah/kamar_tidur/suhu"


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[SUBSCRIBER] Terhubung ke broker {BROKER_ADDRESS}:{BROKER_PORT}")
        client.subscribe(TOPIC, qos=0)
        print(f"[SUBSCRIBER] Berhasil subscribe ke topik '{TOPIC}'")
    else:
        print(f"[SUBSCRIBER] Gagal terhubung, kode hasil: {rc}")


def on_message(client, userdata, msg):
    print(f"[SUBSCRIBER] Topik: {msg.topic} | Pesan: {msg.payload.decode()} | QoS: {msg.qos}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriber_basic")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_forever()


if __name__ == "__main__":
    main()
