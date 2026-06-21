"""
Skenario 3: Penggunaan Beberapa Topik (Multi-Topic)
Studi Kasus: Smart Room Monitoring

Publisher ini merepresentasikan beberapa sensor pada
beberapa ruangan berbeda di sebuah rumah pintar (CPS),
dengan struktur topik hierarkis:

    rumah/<nama_ruangan>/<jenis_sensor>

Topik yang digunakan:
    rumah/kamar_tidur/suhu
    rumah/kamar_tidur/kelembaban
    rumah/dapur/gas
    rumah/dapur/suhu
"""

import paho.mqtt.client as mqtt
import time
import random

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883

# Daftar topik dan rentang nilai acak yang disimulasikan
SENSOR_TOPICS = {
    "rumah/kamar_tidur/suhu":       (22.0, 30.0),   # derajat Celsius
    "rumah/kamar_tidur/kelembaban": (45.0, 75.0),   # persen
    "rumah/dapur/suhu":              (25.0, 38.0),  # derajat Celsius
    "rumah/dapur/gas":                (0.0, 100.0), # ppm (simulasi)
}


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[PUBLISHER-MULTI] Terhubung ke broker {BROKER_ADDRESS}:{BROKER_PORT}")
    else:
        print(f"[PUBLISHER-MULTI] Gagal terhubung, kode hasil: {rc}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="publisher_multitopic")
    client.on_connect = on_connect

    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_start()

    try:
        while True:
            for topic, (low, high) in SENSOR_TOPICS.items():
                value = round(random.uniform(low, high), 2)
                client.publish(topic, str(value), qos=1)
                print(f"[PUBLISHER-MULTI] {topic} -> {value}")
                time.sleep(0.5)
            print("-" * 50)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[PUBLISHER-MULTI] Dihentikan oleh pengguna.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
