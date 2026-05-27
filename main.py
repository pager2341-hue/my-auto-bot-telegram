import telethon
from telethon import TelegramClient
import asyncio
import os

# API အချက်အလက်များ (အတူတူပင်)
API_ID = 39359433                         
API_HASH = '34e0e459bb9dd046a0ed4db3311ea5b8'          

MYANMAR_TARGETS = [-1003762199457, -1003157381562]
FOREIGN_TARGETS = [-1003828762835]
MY_MYANMAR_CHANNEL = '@abodlppdi'
MY_FOREIGN_CHANNEL = '@ninkopint'

HISTORY_FILE = 'history.txt'

def get_history():
    if not os.path.exists(HISTORY_FILE): return set()
    with open(HISTORY_FILE, 'r') as f: return set(line.strip() for line in f)

def save_history(message_id):
    with open(HISTORY_FILE, 'a') as f: f.write(f"{message_id}\n")

client = TelegramClient('session_userbot', API_ID, API_HASH)

async def main():
    await client.connect()
    history = get_history() 

    # ၁။ မြန်မာကားများအတွက်
    for target in MYANMAR_TARGETS:
        async for message in client.iter_messages(target, limit=5, filter=telethon.tl.types.InputMessagesFilterVideo()):
            if str(message.id) not in history:
                duration = message.file.duration if message.file else 0
                if duration >= 60:
                    # ဗီဒီယိုမတင်ခင် ၃ မိနစ် ကြိုတင်သတိပေးခြင်း
                    await client.send_message(MY_MYANMAR_CHANNEL, "⚠️ ဗီဒီယိုအသစ်တင်တော့မှာဖြစ်လို့ စိတ်အနှောင့်အယှက်မဖြစ်စေရန် Notification များကို ခဏပိတ်ထားပေးပါခင်ဗျာ။ ကျေးဇူးတင်ပါတယ်! ❤️", silent=False)
                    await asyncio.sleep(180) # ၃ မိနစ်စောင့်မည်
                    
                    # ဗီဒီယိုတင်ခြင်း
                    await client.send_file(MY_MYANMAR_CHANNEL, file=message.media, caption="🇲🇲 မြန်မာစာတန်းထိုးရုပ်ရှင်များ ❤️", silent=True)
                    save_history(message.id)
                    await asyncio.sleep(15)

    # ၂။ နိုင်ငံခြားကားများအတွက်
    for target in FOREIGN_TARGETS:
        async for message in client.iter_messages(target, limit=5, filter=telethon.tl.types.InputMessagesFilterVideo()):
            if str(message.id) not in history:
                duration = message.file.duration if message.file else 0
                if duration >= 60:
                    # ဗီဒီယိုမတင်ခင် ၃ မိနစ် ကြိုတင်သတိပေးခြင်း
                    await client.send_message(MY_FOREIGN_CHANNEL, "⚠️ ဗီဒီယိုအသစ်တင်တော့မှာဖြစ်လို့ စိတ်အနှောင့်အယှက်မဖြစ်စေရန် Notification များကို ခဏပိတ်ထားပေးပါခင်ဗျာ။ ကျေးဇူးတင်ပါတယ်! ❤️", silent=False)
                    await asyncio.sleep(180) # ၃ မိနစ်စောင့်မည်
                    
                    # ဗီဒီယိုတင်ခြင်း
                    await client.send_file(MY_FOREIGN_CHANNEL, file=message.media, caption="🍿 Enjoy Your Movies! ❤️", silent=True)
                    save_history(message.id)
                    await asyncio.sleep(15)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
          
