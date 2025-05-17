import telebot


#@bot.message_handler(func=lambda message: True)
#def handle_message(message):
#   user_text = message.text
#   print(user_text)
#@bot.message_handler(commands=['start', 'help'])
#def sendMessage(text):
#    bot.send_message(chat_id,text)
#
#sendMessage("Hello")

bot = telebot.TeleBot("7380073491:AAGWGVAsQTNSKgxnfwN_ap-cKZZ0F6h3sYw")
chat_id = 1655740991
print("Create password|Придумайте пароль: ")
passwd = str(input())
@bot.message_handler(commands=['start', 'help'])
def sendMessage(text):
    bot.send_message(chat_id,text)
sendMessage("Система запущена!")

while True:
    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        user_text = message.text
        ps = passwd
        print(ps)
        print(user_text)
        if user_text == "/off":
            sendMessage("Пример ввода команды для отключения оповещения:/off_паполь")
            sendMessage("Вместо 'пароль' вводите пароль, указанный при запуске системы")
        elif user_text == "/off_"+str(passwd):
            security = open("settings/mode.txt", "w")
            sendMessage("Защита отключена!")
            sendMessage("ВНИМАНИЕ!!! Рекомендуется удалить сообщение с паролем для уменьшения риска рассекречивания текущего пароля")
            sendMessage("Значение защиты не меняется после перезагрузки системы, менять его можно только вручную!")
            print("off")
            security.write("0")
            print("Writed 0")
        elif user_text == "/on":
            security = open("settings/mode.txt", "w")
            sendMessage("Защита включена!")
            print("on")
            security.write("1")
            print("Writed 1")


    bot.polling()
