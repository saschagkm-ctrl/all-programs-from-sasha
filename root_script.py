import telebot
import custom_add

from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
KEY = '8516661521:AAEYAjViNrMFVoLur3gwWR0QyjxYJcnVE20'
bot = telebot.TeleBot(KEY)
id_send = []
i1 = False
i2 = False
i3 = False
i4 = False
i5 = False


@bot.message_handler(commands=['help'])
def help_function(message):
    bot.reply_to(message,'this is Anonim bot, you can write all in anonim mode '
    'or you can say from people, and diferent else!. For start just write this command: /start')

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('add who take message')
    button2 = KeyboardButton('add text message')
    button3 = KeyboardButton('add url button')
    button4 = KeyboardButton('add gift')
    button5 = KeyboardButton('test message')
    button6 = KeyboardButton('help to creator')
    button7 = KeyboardButton('send message')
    keyboard.add(button1,button2,button3,button4,button5,button6,button7)
    
    bot.send_message(message.chat.id, 'Ok let start, chose button', reply_markup=keyboard)
@bot.message_handler(func=lambda message: True)
def take_button(message):
    global i1, i2, i3, i4, i5
    # для зручності це частина з додаванням id
    if message.text == 'add who take message':
        custom_add.set_id(bot,message,id_send)
        i1 = True
    elif message.text == 'add text message':
        custom_add.write_message_text(bot,message)
        i2 = True
    elif message.text == 'add url button':
        custom_add.add_InlineKeyboardButtons(bot,message) #work now
        i3 = True
    elif message.text == 'add gift':
        pass # done to 3
    elif message.text == 'test message':
        custom_add.test_message(bot,message) #done
    elif message.text == 'help to creator':
        pass # done to 2
    elif message.text == 'send message':
        custom_add.send_message(bot,message,id_send) #done on 95/100 %
    else:
        print(False)
        if i1 == True and i2 == False and i3 == False:
            custom_add.set_id(bot,message,id_send)
            custom_add.set_id(bot,message,id_send)
            i1 = False
        if i2 == True and i1 == False and i3 == False:
            custom_add.write_message_text(bot,message)
            custom_add.write_message_text(bot,message)
            i2 = False
        if i3 == True and i2 == False and i1 == False:
            s = custom_add.add_InlineKeyboardButtons(bot,message)
            if s == True:
                custom_add.add_InlineKeyboardButtons(bot,message)
                i3 = False
print('bot start!')
bot.polling()
print('bot exit')