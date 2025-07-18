from telethon import TelegramClient, events
import asyncio

# 🔑 اطلاعات اکانت - این را خودت باید از https://my.telegram.org برداری
api_id = 24447677   # <<== جایگزین کن
api_hash = 'b5b1aee85d98b5e14a66d990472bd09d'  # <<== جایگزین کن
session_name = 'my_session'  # یک نام دلخواه برای فایل سشن

# 📌 لیست کلمات کلیدی
keywords = [
    'machine learning', 'deep learning', 'regression', 'AI', 'ماشین لرنینگ',
    'یادگیری ماشین', 'data science', 'عصبی', 'یادگیری عمیق', 'هوش مصنوعی',
    'تحلیل داده', 'علوم کامپیوتر', 'علوم داده', 'Machine learning',
    'Deep learning', 'Regression', 'ai', 'Ai', 'Data science', 'دیپ لرنینگ',
    'تحلیلگر','پایتون','برنامه نویس','ماشین','لرنینگ','زبان R','مهندس کامپیوتر',
    'کامپیوتر','زبان طبیعی','nlp','NLP','بینایی ماشین','یادگیری تقویتی','vision',
    'reinforcement','Reinforcement','الگوریتم'
]

# 📨 آی‌دی مقصد
forward_to = '@Amir_GH_0505'


async def main():
    client = TelegramClient(session_name, api_id, api_hash)

    await client.start()  # فقط بار اول ازت کد می‌خواد

    print("✅ Logged in successfully.")

    @client.on(events.NewMessage)
    async def handler(event):
        try:
            message_text = event.message.message.lower()
            if any(keyword.lower() in message_text for keyword in keywords):
                await client.forward_messages(forward_to, event.message)
                print(f"📤 Forwarded: {message_text}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    print("📡 Listening for new messages...")
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
