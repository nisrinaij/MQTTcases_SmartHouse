"""
Skenario 4: Penggunaan Wildcard '+'
Studi Kasus: Smart Room Monitoring

Wildcard '+' menggantikan TEPAT SATU level topik.

Contoh:
    Subscribe ke: rumah/+/suhu

Maka subscriber ini akan menerima pesan dari:
    rumah/ruang_tamu/suhu
    rumah/kamar_tidur/suhu
    rumah/dapur/suhu

Tetapi TIDAK akan menerima pesan dari:
    rumah/ruang_tamu/kelembaban   (karena level terakhir bukan 'suhu')
    rumah/dapur/gas               (karena level terakhir bukan 'suhu')

Gunakan bersamaan dengan 03_publisher_multitopic.py
untuk melihat hasilnya.
"""

import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC_FILTER = "rumah/+/suhu"


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[SUBSCRIBER-WILDCARD+] Terhubung ke broker {BROKER_ADDRESS}:{BROKER_PORT}")
        client.subscribe(TOPIC_FILTER, qos=0)
        print(f"[SUBSCRIBER-WILDCARD+] Subscribe ke filter '{TOPIC_FILTER}'")
        print("[SUBSCRIBER-WILDCARD+] Hanya akan menerima data SUHU dari semua ruangan")
    else:
        print(f"[SUBSCRIBER-WILDCARD+] Gagal terhubung, kode hasil: {rc}")


def on_message(client, userdata, msg):
    # msg.topic akan berisi topik asli yang sebenarnya, misal rumah/dapur/suhu
    bagian = msg.topic.split("/")
    ruangan = bagian[1] if len(bagian) > 1 else "?"
    print(f"[SUBSCRIBER-WILDCARD+] Ruangan='{ruangan}' | Topik='{msg.topic}' "
          f"| Suhu={msg.payload.decode()} °C")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriber_wildcard_plus")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_forever()


if __name__ == "__main__":
    main()
