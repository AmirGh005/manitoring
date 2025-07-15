from telethon import TelegramClient, events
import asyncio

# --- اطلاعات شما ---
api_id = 24447677  # جایگزین کن با API ID خودت
api_hash = 'b5b1aee85d98b5e14a66d990472bd09d'  # جایگزین کن با API Hash
session_name = 'amir_session'  # فایل session ذخیره میشه

# --- عبارات مورد نظر ---
keywords = [
    'machine learning', 'deep learning', 'regression', 'AI', 'ماشین لرنینگ',
    'یادگیری ماشین', 'data science', 'عصبی', 'یادگیری عمیق', 'هوش مصنوعی',
    'تحلیل داده', 'علوم کامپیوتر', 'علوم داده', 'Machine learning',
    'Deep learning', 'Regression', 'ai', 'Ai', 'Data science', 'دیپ لرنینگ',
    'تحلیلگر','پایتون','برنامه نویس','ماشین','لرنینگ','زبان R','مهندس کامپیوتر',
    'کامپیوتر','زبان طبیعی','nlp','NLP','بینایی ماشین','یادگیری تقویتی','vision',
    'reinforcement','Reinforcement','الگوریتم'
]

# --- مقصد فوروارد ---
forward_to = '@Amir_GH_0505'

# --- ساختن کلاینت ---
client = TelegramClient(session_name, api_id, api_hash)

# --- هندل کردن پیام‌ها ---
@client.on(events.NewMessage)
async def handler(event):
    if event.message.message:  # اگر پیام متنی بود
        message_text = event.message.message.lower()
        if any(word.lower() in message_text for word in keywords):
            try:
                await event.message.forward_to(forward_to)
                print(f'✅ پیام فروارد شد: {message_text}')
            except Exception as e:
                print(f'❌ خطا در فوروارد: {e}')

# --- اجرای برنامه ---
async def main():
    await client.start()
    print("🚀 ربات فعال است و منتظر پیام‌های جدید...")
    await client.run_until_disconnected()

# شروع
if __name__ == '__main__':
    asyncio.run(main())
