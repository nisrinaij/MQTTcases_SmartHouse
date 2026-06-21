"""
Skenario 1: Komunikasi Dasar Publisher-Subscriber
Studi Kasus: Smart Room Monitoring

Publisher ini mengirim data suhu ruangan secara berkala
ke topik: rumah/kamar_tidur/suhu
"""

import paho.mqtt.client as mqtt
import time
import random

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "rumah/kamar_tidur/suhu"


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[PUBLISHER] Terhubung ke broker {BROKER_ADDRESS}:{BROKER_PORT}")
    else:
        print(f"[PUBLISHER] Gagal terhubung, kode hasil: {rc}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="publisher_basic")
    client.on_connect = on_connect

    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_start()

    try:
        while True:
            suhu = round(random.uniform(24.0, 32.0), 2)
            payload = f"{suhu}"
            client.publish(TOPIC, payload, qos=0)
            print(f"[PUBLISHER] Mengirim ke '{TOPIC}': {payload} °C")
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n[PUBLISHER] Dihentikan oleh pengguna.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
