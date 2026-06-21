# Implementasi Komunikasi MQTT — Smart Room Monitoring

Proyek ini berisi implementasi komunikasi MQTT menggunakan Python (paho-mqtt)
dan Mosquitto Broker untuk studi kasus **Smart Room Monitoring**.

## 1. Instalasi Mosquitto Broker

### Windows
1. Unduh installer dari https://mosquitto.org/download/
2. Install, lalu jalankan Mosquitto sebagai service

## 2. Instalasi Library Python
```bash
pip install paho-mqtt
```

## 3. Struktur Topik (Desain Sistem CPS)

```
rumah/
├── kamar_tidur/
│   ├── suhu
│   └── kelembaban
└── dapur/
    ├── suhu
    └── gas
```

## 4. Daftar Skenario & Cara Menjalankan

Jalankan setiap pasangan publisher/subscriber pada terminal terpisah.

### Skenario 1 — Komunikasi Dasar
```bash
python 01_subscriber_basic.py
python 01_publisher_basic.py
```
Topik: `rumah/kamar_tidur/suhu` (QoS 0)

### Skenario 2 — Variasi QoS (0, 1, 2)
```bash
python 02_subscriber_qos.py
python 02_publisher_qos.py
```
Topik: `rumah/kamar_tidur/kelembaban`
Publisher bergiliran mengirim dengan QoS 0, 1, dan 2.

### Skenario 3 — Multi Topik
```bash
python 03_subscriber_multitopic.py
python 03_publisher_multitopic.py
```
Mensimulasikan beberapa sensor pada beberapa ruangan.

### Skenario 4 — Wildcard `+`
```bash
python 04_subscriber_wildcard_plus.py
python 03_publisher_multitopic.py
```
Filter: `rumah/+/suhu` — hanya menerima data suhu dari semua ruangan.

### Skenario 5 — Wildcard `#`
```bash
python 05_subscriber_wildcard_hash.py
python 03_publisher_multitopic.py
```
Filter: `rumah/#` — menerima seluruh data sensor di hierarki rumah.

## 5. Pengujian QoS

Untuk menguji efek QoS secara nyata (misalnya pesan hilang saat
koneksi terputus), dapat dilakukan dengan:
1. Menjalankan subscriber, lalu memutus koneksi internet/jaringan sebentar.
2. Menjalankan publisher dengan QoS 1 atau 2 saat subscriber offline.
3. Menyambungkan kembali subscriber dan mengamati apakah pesan
   yang "tertunda" diterima (untuk QoS 1/2 dengan `clean_session=False`
   dan `session_expiry_interval` yang sesuai).
