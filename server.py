from bot import telegram_chatbot
import daVinci
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
            reply, mode = daVinci.make_reply(message)
            if mode == 1:
                bot.send_image(reply, from_)
            else: # text
                bot.send_message(reply, from_)
