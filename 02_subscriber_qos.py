"""
Skenario 2: Pengiriman Data dengan QoS Berbeda (QoS 0, 1, 2)
Studi Kasus: Smart Room Monitoring

Subscriber ini melakukan subscribe dengan QoS=2 (QoS tertinggi
yang diminta subscriber) ke topik: rumah/kamar_tidur/kelembaban

Catatan:
QoS efektif suatu pesan adalah nilai MINIMUM antara
QoS publisher dan QoS subscriber.
"""

import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "rumah/kamar_tidur/kelembaban"
SUBSCRIBE_QOS = 2


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[SUBSCRIBER-QOS] Terhubung ke broker {BROKER_ADDRESS}:{BROKER_PORT}")
        client.subscribe(TOPIC, qos=SUBSCRIBE_QOS)
        print(f"[SUBSCRIBER-QOS] Subscribe ke '{TOPIC}' dengan QoS={SUBSCRIBE_QOS}")
    else:
        print(f"[SUBSCRIBER-QOS] Gagal terhubung, kode hasil: {rc}")


def on_message(client, userdata, msg):
    print(f"[SUBSCRIBER-QOS] Topik: {msg.topic} | Pesan: {msg.payload.decode()}% "
          f"| QoS pesan diterima: {msg.qos} | retain: {msg.retain}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriber_qos")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_forever()


if __name__ == "__main__":
    main()
