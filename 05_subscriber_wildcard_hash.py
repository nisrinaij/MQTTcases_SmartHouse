"""
Skenario 5: Penggunaan Wildcard '#'
Studi Kasus: Smart Room Monitoring

Wildcard '#' menggantikan SATU ATAU LEBIH level topik
di posisi akhir (multi-level wildcard), dan harus
menjadi karakter TERAKHIR pada topic filter.

Contoh:
    Subscribe ke: rumah/#

Maka subscriber ini akan menerima SEMUA pesan di bawah
hierarki 'rumah/', termasuk:
    rumah/ruang_tamu/suhu
    rumah/ruang_tamu/kelembaban
    rumah/kamar_tidur/suhu
    rumah/kamar_tidur/kelembaban
    rumah/dapur/suhu
    rumah/dapur/gas
    rumah/lantai2/kamar1/suhu  (sub-level lebih dalam pun tetap diterima)

Gunakan bersamaan dengan 03_publisher_multitopic.py
untuk melihat hasilnya. Subscriber ini berfungsi sebagai
"dashboard pusat" yang memantau SELURUH sensor di rumah.
"""

import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC_FILTER = "rumah/#"


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[SUBSCRIBER-WILDCARD#] Terhubung ke broker {BROKER_ADDRESS}:{BROKER_PORT}")
        client.subscribe(TOPIC_FILTER, qos=0)
        print(f"[SUBSCRIBER-WILDCARD#] Subscribe ke filter '{TOPIC_FILTER}'")
        print("[SUBSCRIBER-WILDCARD#] Akan menerima SEMUA data sensor di hierarki 'rumah/'")
    else:
        print(f"[SUBSCRIBER-WILDCARD#] Gagal terhubung, kode hasil: {rc}")


def on_message(client, userdata, msg):
    print(f"[SUBSCRIBER-WILDCARD#] Topik='{msg.topic}' | Nilai={msg.payload.decode()}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriber_wildcard_hash")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_forever()


if __name__ == "__main__":
    main()
