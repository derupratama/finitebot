from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TOKEN")
import hashlib

# =====================================
# DFA STATES
# =====================================
# q0  = Idle / Start
# q1  = Menu
# q2  = Mode String
# q3  = Mode Gambar
# q5  = Mode Password

# q6  = Accept String
# q8  = Accept Gambar
# q10 = Accept Password

# =====================================
# MEMORY USER STATE
# =====================================
user_states = {}

# =====================================
# /start
# =====================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    user_states[user_id] = "q0"

    text = """
STATE SEKARANG : q0
STATUS         : ACCEPTED

Mesin DFA aktif.

Gunakan:
/menu

untuk memulai mesin.
"""

    await update.message.reply_text(text)

# =====================================
# /menu
# =====================================
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    previous_state = user_states.get(user_id, "q0")

    user_states[user_id] = "q1"

    text = f"""
STATE SEKARANG : q1
TRANSISI       : {previous_state} -> q1
STATUS         : ACCEPTED

MENU MESIN DFA

1 = Pembalik String
2 = Gambar
3 = Password MD5

Masukkan:
1 / 2 / 3
"""

    await update.message.reply_text(text)

# =====================================
# HANDLE INPUT
# =====================================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    message = update.message.text

    current_state = user_states.get(user_id, "q0")

    # =====================================
    # q0
    # =====================================
    if current_state == "q0":

        text = f"""
STATE SEKARANG : q0
STATUS         : REJECTED

INPUT:
{message}

Input tidak dimengerti mesin.

Gunakan:
/menu
"""

        await update.message.reply_text(text)

        return

    # =====================================
    # q1 = MENU
    # =====================================
    if current_state == "q1":

        if message == "1":

            user_states[user_id] = "q2"

            text = """
STATE SEKARANG : q2
TRANSISI       : q1 -> q2
STATUS         : ACCEPTED

MODE PEMBALIK STRING

Gunakan:

/string teks
"""

            await update.message.reply_text(text)

        elif message == "2":

            user_states[user_id] = "q3"

            text = """
STATE SEKARANG : q3
TRANSISI       : q1 -> q3
STATUS         : ACCEPTED

MODE GAMBAR

Pilihan:
1 = Kucing
2 = Jerapah
3 = Singa

Gunakan:

/gambar 1
/gambar 2
/gambar 3
"""

            await update.message.reply_text(text)

        elif message == "3":

            user_states[user_id] = "q5"

            text = """
STATE SEKARANG : q5
TRANSISI       : q1 -> q5
STATUS         : ACCEPTED

MODE PASSWORD MD5

Gunakan:

/password teks
"""

            await update.message.reply_text(text)

        else:

            text = f"""
STATE SEKARANG : q1
STATUS         : REJECTED

INPUT:
{message}

Pilihan hanya:
1
2
3

Mesin kembali ke q0.
"""

            await update.message.reply_text(text)

            user_states[user_id] = "q0"

        return

    # =====================================
    # q2 = STRING
    # =====================================
    if current_state == "q2":

        if message.startswith("/string "):

            original = message.replace("/string ", "")

            reversed_text = original[::-1]

            user_states[user_id] = "q6"

            text = f"""
STATE SEKARANG : q6
TRANSISI       : q2 -> q6
STATUS         : ACCEPTED

INPUT:
{message}

String asli:
{original}

Hasil:
{reversed_text}

Mesin kembali ke q0.
"""

            await update.message.reply_text(text)

            user_states[user_id] = "q0"

        else:

            text = f"""
STATE SEKARANG : q2
STATUS         : REJECTED

INPUT:
{message}

Gunakan:
/string teks

Mesin kembali ke q0.
"""

            await update.message.reply_text(text)

            user_states[user_id] = "q0"

        return

    # =====================================
    # q3 = GAMBAR
    # =====================================
    if current_state == "q3":

        if message == "/gambar 1":

            user_states[user_id] = "q8"

            photo = open("images/kucing.png", "rb")

            await update.message.reply_photo(
                photo=photo,
                caption=f"""
STATE SEKARANG : q8
TRANSISI       : q3 -> q8
STATUS         : ACCEPTED

INPUT:
{message}

ANDA MEMILIH:
KUCING

Mesin kembali ke q0.
"""
            )

            user_states[user_id] = "q0"

        elif message == "/gambar 2":

            user_states[user_id] = "q8"

            photo = open("images/jerapah.jpg", "rb")

            await update.message.reply_photo(
                photo=photo,
                caption=f"""
STATE SEKARANG : q8
TRANSISI       : q3 -> q8
STATUS         : ACCEPTED

INPUT:
{message}

ANDA MEMILIH:
JERAPAH

Mesin kembali ke q0.
"""
            )

            user_states[user_id] = "q0"

        elif message == "/gambar 3":

            user_states[user_id] = "q8"

            photo = open("images/singa.jpg", "rb")

            await update.message.reply_photo(
                photo=photo,
                caption=f"""
STATE SEKARANG : q8
TRANSISI       : q3 -> q8
STATUS         : ACCEPTED

INPUT:
{message}

ANDA MEMILIH:
SINGA

Mesin kembali ke q0.
"""
            )

            user_states[user_id] = "q0"

        else:

            text = f"""
STATE SEKARANG : q3
STATUS         : REJECTED

INPUT:
{message}

Gunakan:
- /gambar 1
- /gambar 2
- /gambar 3

Mesin kembali ke q0.
"""

            await update.message.reply_text(text)

            user_states[user_id] = "q0"

        return

    # =====================================
    # q5 = PASSWORD
    # =====================================
    if current_state == "q5":

        if message.startswith("/password "):

            raw = message.replace("/password ", "")

            result = hashlib.md5(raw.encode()).hexdigest()

            user_states[user_id] = "q10"

            text = f"""
STATE SEKARANG : q10
TRANSISI       : q5 -> q10
STATUS         : ACCEPTED

INPUT:
{message}

TEXT:
{raw}

HASIL MD5:
{result}

Mesin kembali ke q0.
"""

            await update.message.reply_text(text)

            user_states[user_id] = "q0"

        else:

            text = f"""
STATE SEKARANG : q5
STATUS         : REJECTED

INPUT:
{message}

Gunakan:
/password teks

Mesin kembali ke q0.
"""

            await update.message.reply_text(text)

            user_states[user_id] = "q0"

        return

# =====================================
# MAIN
# =====================================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

app.add_handler(
    MessageHandler(filters.COMMAND, handle_message)
)

print("BOT DFA BERJALAN...")
app.run_polling()
