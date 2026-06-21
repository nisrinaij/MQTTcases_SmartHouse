"""
Skenario 3: Penggunaan Beberapa Topik (Multi-Topic)
Studi Kasus: Smart Room Monitoring

Subscriber ini melakukan subscribe ke beberapa topik
spesifik secara terpisah (tanpa wildcard) untuk
menunjukkan bagaimana sebuah aplikasi monitoring dapat
memantau beberapa sensor sekaligus.
"""

import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883

TOPICS = [
    ("rumah/kamar_tidur/suhu", 0),
    ("rumah/kamar_tidur/kelembaban", 0),
    ("rumah/dapur/suhu", 0),
    ("rumah/dapur/gas", 1),
]


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[SUBSCRIBER-MULTI] Terhubung ke broker {BROKER_ADDRESS}:{BROKER_PORT}")
        client.subscribe(TOPICS)
        for topic, qos in TOPICS:
            print(f"[SUBSCRIBER-MULTI] Subscribe -> {topic} (QoS {qos})")
    else:
        print(f"[SUBSCRIBER-MULTI] Gagal terhubung, kode hasil: {rc}")


def on_message(client, userdata, msg):
    print(f"[SUBSCRIBER-MULTI] {msg.topic} = {msg.payload.decode()}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriber_multitopic")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_forever()


if __name__ == "__main__":
    main()
