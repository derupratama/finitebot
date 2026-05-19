# 🤖 Telegram DFA Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)
![DFA](https://img.shields.io/badge/Theory-DFA-black?style=for-the-badge)
![License](https://img.shields.io/badge/Project-TBO-success?style=for-the-badge)

### Implementasi Deterministic Finite Automata (DFA) pada Chatbot Telegram Berbasis Command Parser

</div>

---

# 📌 Deskripsi Project

Project ini merupakan implementasi **Deterministic Finite Automata (DFA)** pada sistem chatbot Telegram berbasis command parser.

Bot bekerja seperti mesin automata yang:
- menerima input command,
- membaca pola input,
- melakukan transisi state,
- menentukan apakah input diterima (*accepted*) atau ditolak (*rejected*).

Project ini dibuat untuk memenuhi tugas mata kuliah **Teori Bahasa dan Otomata (TBO)**.

---

# 🎯 Fitur Bot

Bot memiliki beberapa fitur utama:

| Command | Fungsi | Status |
|---|---|---|
| `/menu` | Menampilkan menu utama | Accepted |
| `/string teks` | Membalik string | Accepted |
| `/string` | String kosong | Rejected |
| `/gambar 1` | Menampilkan gambar gajah | Accepted |
| `/gambar 2` | Menampilkan gambar jerapah | Accepted |
| `/gambar 3` | Menampilkan gambar singa | Accepted |
| `/gambar selain 1-3` | Input salah | Rejected |
| `/password teks` | Menghasilkan hash MD5 | Accepted |
| `/password` | Password kosong | Rejected |

---

# 🧠 Konsep DFA

Bot ini menggunakan konsep **Deterministic Finite Automata**.

## State DFA

| State | Keterangan |
|---|---|
| `q0` | Menunggu command |
| `q1` | Menu utama |
| `q2` | Pembalik string |
| `q3` | Menu gambar |
| `q4` | Password MD5 |
| `q_accept` | Input diterima |
| `q_reject` | Input ditolak |

---

# 🔄 Alur DFA

```text
q0 -- /menu --> q1

q1 -- /string teks --> q2 --> q_accept
q1 -- /string kosong --> q_reject

q1 -- /gambar 1/2/3 --> q3 --> q_accept
q1 -- /gambar selain 1/2/3 --> q_reject

q1 -- /password teks --> q4 --> q_accept
q1 -- /password kosong --> q_reject
```

---

# 📂 Struktur Folder

```text
bot/
│
├── bot.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── images/
│   ├── gajah.jpg
│   ├── jerapah.jpg
│   └── singa.jpg
```

---

# ⚙️ Instalasi Project

## 1. Clone Repository

```bash
git clone https://github.com/username/repository.git
```

---

## 2. Masuk ke Folder Project

```bash
cd bot
```

---

## 3. Membuat Virtual Environment

### Windows

```bash
python -m venv .venv
```

### Linux / Mac

```bash
python3 -m venv .venv
```

---

## 4. Mengaktifkan Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 5. Install Dependency

```bash
pip install -r requirements.txt
```

---

# 🔐 Konfigurasi TOKEN Telegram

## 1. Buat Bot Telegram

Buka:

👉 https://t.me/BotFather

Lalu gunakan command:

```text
/newbot
```

Ikuti instruksi hingga mendapatkan TOKEN.

---

## 2. Copy File Environment

### Windows

```bash
copy .env.example .env
```

### Linux / Mac

```bash
cp .env.example .env
```

---

## 3. Isi TOKEN pada `.env`

```env
TOKEN=ISI_TOKEN_BOT_TELEGRAM
```

---

# ▶️ Menjalankan Bot

```bash
python bot.py
```

Jika berhasil:

```text
BOT BERJALAN...
```

---

# 🖼️ Contoh Penggunaan

## Menu

```text
/menu
```

---

## Pembalik String

```text
/string halo dunia
```

Output:

```text
ainud olah
```

---

## Menu Gambar

```text
/gambar 1
```

Bot akan menampilkan gambar gajah.

---

## Password MD5

```text
/password admin123
```

Output:

```text
0192023a7bbd73250516f069df18b500
```

---

# ❌ Contoh Rejected State

## Input Salah

```text
/gambar 9
```

Output:

```text
STATE: q_reject
STATUS: REJECTED
```

---

# 🧪 Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| Telegram Bot API | API chatbot Telegram |
| python-telegram-bot | Library Telegram |
| hashlib | Generate hash MD5 |
| dotenv | Menyimpan environment variable |

---

# 📚 Implementasi TBO

Project ini mengimplementasikan:

- Deterministic Finite Automata (DFA)
- State Machine
- Command Parser
- Accept / Reject State
- Transition Function
- Input Validation

---

# 🚀 Cara Kerja Bot

1. User mengirim command.
2. Bot membaca input.
3. Sistem mengecek format command.
4. DFA menentukan state berikutnya.
5. Jika input valid → accepted.
6. Jika input salah → rejected.

---

# 📖 Teori DFA

DFA didefinisikan dengan 5 tupel:

```text
M = (Q, Σ, δ, S, F)
```

Dimana:

- `Q` = himpunan state
- `Σ` = himpunan input
- `δ` = fungsi transisi
- `S` = state awal
- `F` = final state

---

# 📌 Catatan

- File `.env` tidak diupload demi keamanan TOKEN.
- Virtual environment `.venv` tidak disertakan.
- Gunakan `.env.example` sebagai template konfigurasi.

---

# 👨‍💻 Author

### Deru Pratama
### Nizam Al- Gifari

Project Mata Kuliah:
**Teori Bahasa dan Otomata**

---

# ⭐ Penutup

Project ini membuktikan bahwa konsep **Deterministic Finite Automata (DFA)** tidak hanya digunakan pada teori formal, tetapi juga dapat diimplementasikan pada sistem nyata seperti chatbot Telegram berbasis command parser.

---
