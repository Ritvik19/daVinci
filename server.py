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
            if reply is None:
                bot.send_message('Something went wrong', from_)
            else:
                if mode == 0:
                    bot.send_message(reply, from_)
                elif mode == 1:
                    bot.send_markdown(reply, from_)
                elif mode == 2:
                    bot.send_image(reply, from_)
                elif mode == 3:
                    bot.send_image(reply[1], from_)
                    bot.send_message(reply[0], from_)
                elif mode == 4:
                    bot.send_message(reply[0], from_)
                    bot.send_markup(reply[1], from_)
