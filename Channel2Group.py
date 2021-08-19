TELEGRAM_API_ID = your id
TELEGRAM_API_HASH = "your token"


COMBINATIONS = {  chat id of the channel: [chat id of the group]  }
from telethon import TelegramClient, events
# from settings import TELEGRAM_API_ID, TELEGRAM_API_HASH, COMBINATIONS
 
 
client = TelegramClient('session', api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH)
 
 
@client.on(events.NewMessage)
async def handle_new_message(event):
    sender_chat_id = event.sender_id
    if sender_chat_id in list(COMBINATIONS.keys()):
        destination_chat_ids = COMBINATIONS.get(sender_chat_id, [])
        for chat_id in destination_chat_ids:
             await client.send_message(chat_id, event.raw_text)
 
client.start()
client.run_until_disconnected()



# Sam Son, [19.08.21 17:36]
