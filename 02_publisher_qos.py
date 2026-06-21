"""
Skenario 2: Pengiriman Data dengan QoS Berbeda (QoS 0, 1, 2)
Studi Kasus: Smart Room Monitoring

Publisher ini mengirimkan data sensor kelembaban ruangan
dengan tiga tingkat QoS yang berbeda secara bergiliran
ke topik: rumah/kamar_tidur/kelembaban

QoS 0 -> At most once  (kirim sekali, tidak ada konfirmasi)
QoS 1 -> At least once (kirim hingga ada PUBACK, bisa duplikat)
QoS 2 -> Exactly once  (handshake 4 langkah, dijamin sekali sampai)
"""

import paho.mqtt.client as mqtt
import time
import random

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "rumah/kamar_tidur/kelembaban"


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[PUBLISHER-QOS] Terhubung ke broker {BROKER_ADDRESS}:{BROKER_PORT}")
    else:
        print(f"[PUBLISHER-QOS] Gagal terhubung, kode hasil: {rc}")


def on_publish(client, userdata, mid, reason_code=None, properties=None):
    print(f"[PUBLISHER-QOS] Pesan dengan message-id {mid} terkonfirmasi terkirim")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="publisher_qos")
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_start()

    qos_levels = [0, 1, 2]

    try:
        counter = 0
        while True:
            qos = qos_levels[counter % len(qos_levels)]
            kelembaban = round(random.uniform(40.0, 70.0), 2)
            payload = f"{kelembaban}"

            result = client.publish(TOPIC, payload, qos=qos)
            print(f"[PUBLISHER-QOS] QoS={qos} | Topik='{TOPIC}' | Pesan={payload}% "
                  f"| message-id={result.mid}")

            counter += 1
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n[PUBLISHER-QOS] Dihentikan oleh pengguna.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
