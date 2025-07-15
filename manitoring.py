import os
import base64
import asyncio
from telethon import TelegramClient, events

# --- اطلاعات حساب ---
api_id = 24447677  # ← جایگزین کن
api_hash = 'b5b1aee85d98b5e14a66d990472bd09d'  # ← جایگزین کن

# --- بازیابی session از secret (در GitHub Actions) ---
if os.getenv('TG_SESSION_B64'):
    with open('gh_session.session', 'wb') as f:
        f.write(base64.b64decode(os.getenv('TG_SESSION_B64')))

client = TelegramClient('gh_session', api_id, api_hash)

# --- کلیدواژه‌ها و مقصد ---
keywords = [
    'machine learning', 'deep learning', 'regression', 'AI', 'ماشین لرنینگ',
    'یادگیری ماشین', 'data science', 'عصبی', 'یادگیری عمیق', 'هوش مصنوعی',
    'تحلیل داده', 'علوم کامپیوتر', 'علوم داده', 'Machine learning',
    'Deep learning', 'Regression', 'ai', 'Ai', 'Data science', 'دیپ لرنینگ',
    'تحلیلگر','پایتون','برنامه نویس','ماشین','لرنینگ','زبان R','مهندس کامپیوتر',
    'کامپیوتر','زبان طبیعی','nlp','NLP','بینایی ماشین','یادگیری تقویتی','vision',
    'reinforcement','Reinforcement','الگوریتم'
]
forward_to = '@Amir_GH_0505'

@client.on(events.NewMessage)
async def handler(event):
    if event.message.message:
        text = event.message.message.lower()
        if any(word.lower() in text for word in keywords):
            try:
                await event.message.forward_to(forward_to)
                print("✅ پیام فروارد شد")
            except Exception as e:
                print("❌ خطا در فوروارد:", e)

async def main():
    await client.start()
    print("🚀 ربات آماده دریافت پیام است...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())

