# Telegram DFA Chatbot

Project ini merupakan implementasi Deterministic Finite Automata (DFA) pada chatbot Telegram berbasis command parser.

## Fitur

Bot memiliki beberapa fitur utama, berupa:

1. Pembalik String
   - Command:
   ```bash
   /string teks
   ```

2. Gambar
   - Command:
   ```bash
   /gambar 1
   /gambar 2
   /gambar 3
   ```

3. Password MD5
   - Command:
   ```bash
   /password teks
   ```

---

## Konsep DFA

State yang digunakan:

- q0 = menunggu command
- q1 = menu utama
- q2 = pembalik string
- q3 = gambar
- q4 = password md5
- q_accept = input diterima
- q_reject = input ditolak

---

## Instalasi

### Clone repository

```bash
git clone https://github.com/derupratama/finitebot.git
```

---

### Masuk folder project

```bash
cd finitebot
```

---

### Buat virtual environment

```bash
python -m venv .venv
```

---

### Aktifkan virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

---

### Install dependency

```bash
pip install -r requirements.txt
```

---

## Buat Env

Buat file `.env`

```bash
cp .env.example .env
```

## Konfigurasi Env buat Bot Telegram dan masukkan Token

```env
TOKEN=ISI_TOKEN_TELEGRAM
```

---

## Menjalankan Bot

```bash
python bot.py
```

Jika berhasil:

```bash
BOT BERJALAN...
```

---

## Struktur Folder

```txt
bot/
│
├── bot.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── images/
│   ├── gajah.jpg
│   ├── jerapah.jpg
│   └── singa.jpg
│
└── .env
```

---

## Teknologi

- Python
- Telegram Bot API
- python-telegram-bot
- DFA (Deterministic Finite Automata)

---

## Author

Deru Pratama
Nizam Al- Gifari
