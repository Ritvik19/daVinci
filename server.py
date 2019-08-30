from bot import telegram_chatbot
from daVinci import make_reply
bot = telegram_chatbot("E:/daVinci/config.cfg")

update_id = None
print('The Server is running')
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
