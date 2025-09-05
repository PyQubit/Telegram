# PyQubit AI Telegram Bot 🤖

**Developer:** Mohammad Mahdi Omidvar

© 2025 Mohammad Mahdi Omidvar

---

## 🌟 Features | امکانات

* AI chatbot powered by **Gemma 3:4b**
* چت‌بات هوشمند با استفاده از **Gemma 3:4b**
* Stores chat history in **SQLite**
* ذخیره تاریخچه پیام‌ها در **SQLite**
* Multi-user support via Telegram
* پشتیبانی از چند کاربر در تلگرام
* Streaming response from AI model
* پاسخ‌ها به صورت زنده و جریان داده می‌شوند

---

## 🛠️ Installation | نصب

### Requirements | پیش‌نیازها

* Python 3.13+
* Telegram Bot API token
* Ollama CLI installed and running
* Gemma 3:4b model installed

### Python Libraries | کتابخانه‌های پایتون

```bash
pip install python-telegram-bot==20.4 ollama db-sqlite3
```

---

### AI Model | مدل هوش مصنوعی

Install **Gemma 3:4b** locally:

```bash
ollama pull gemma3:4b
```

* This is the main AI model for the chatbot
* مدل اصلی چت‌بات
* Make sure **Ollama CLI** is installed and active
* حتماً Ollama CLI نصب و فعال باشد

---

## 🚀 How to Run | نحوه اجرا

1. **Set your Telegram bot token** in the script:

```python
application = Application.builder().token('Your_Token').build()
```

2. **Run the bot**:


3. **Start chatting** by sending `/start` in your Telegram bot

---

## 💾 Database | پایگاه داده

* Uses `chat_history.db` (SQLite)
* ذخیره پیام‌های کاربر و پاسخ‌های AI
* Stores last 10 messages per user for context
* ذخیره آخرین ۱۰ پیام برای هر کاربر برای حفظ زمینه گفتگو

---

## 📝 How it works | نحوه عملکرد

1. User sends a message in Telegram / کاربر پیامی ارسال می‌کند
2. Message is stored in SQLite / پیام در دیتابیس ذخیره می‌شود
3. Last 10 messages are sent to **Gemma 3:4b** via Ollama / آخرین ۱۰ پیام به مدل **Gemma 3:4b** ارسال می‌شود
4. AI generates a streaming response / هوش مصنوعی پاسخ جریان‌دار تولید می‌کند
5. Response is saved and sent back to the user / پاسخ ذخیره و برای کاربر ارسال می‌شود

---

## ⚠️ Notes | نکات مهم

* Developer: Mohammad Mahdi Omidvar
* Make sure all Python libraries and Gemma 3:4b model are installed before running
* تمام کتابخانه‌ها و مدل Gemma 3:4b باید قبل از اجرا نصب شده باشند
* Database file `chat_history.db` will be created automatically
* فایل دیتابیس `chat_history.db` به صورت خودکار ایجاد می‌شود

---

## 🌐 Connect with Me | ارتباط با من

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram\&logoColor=white\&style=for-the-badge)](https://instagram.com/PyQubit)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?logo=telegram\&logoColor=white\&style=for-the-badge)](https://t.me/PyQubit)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail\&logoColor=white\&style=for-the-badge)](mailto:pyqubit@gmail.com)

---

© 2025 **Mohammad Mahdi Omidvar**
