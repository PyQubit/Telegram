#PyQubit AI Bot

#pip install python-telegram-bot==20.4 ollama db-sqlite3
#Get your token from @BotFather
#ollama pull gemma3:4b

#Developer : Mohammad Mahdi Omidvar 


import logging
from telegram import Update, InputFile
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
from ollama import chat
import sqlite3

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


SYSTEM_PROMPT = '''     
Your name is PyQubit and you are a AI
'''

def init_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_message(user_id, role, content):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('INSERT INTO conversations (user_id, role, content) VALUES (?, ?, ?)', 
              (user_id, role, content))
    conn.commit()
    conn.close()

def get_conversation_history(user_id, limit=10):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('SELECT role, content FROM conversations WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?', 
              (user_id, limit))
    history = [{'role': row[0], 'content': row[1]} for row in c.fetchall()]
    conn.close()
    return history[::-1]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('DELETE FROM conversations WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
    
    with open('1.jpg', 'rb') as photo:
        await update.message.reply_photo(
            photo=photo,
            caption='Hi welcome to PyQubit AI \n\n Develper : @PyQubit'
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    logger.info(f"User {user_id}: {text}")
    save_message(user_id, 'user', text)
    conversation_history = get_conversation_history(user_id, limit=10)
    messages = [{'role': 'system', 'content': SYSTEM_PROMPT}] + conversation_history
    

    stream = chat(
        model='gemma3:4b',
        messages=messages,
        stream=True
    )
    response = ""
    for chunk in stream:
        response += chunk['message']['content']
    

    save_message(user_id, 'assistant', response)

    await update.message.reply_text(response)

def main():
    init_db()
    
    application = Application.builder().token('Your_Token').build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info('START')
    application.run_polling()

if __name__ == '__main__':
    main()