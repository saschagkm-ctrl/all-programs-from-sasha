import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# set_id-----------------------
active_for_set_id: bool = False
messagestr_for_set_id = []
i = []
# send_text and write_text and test_message
text_to_send = []
messagestr_for_write_message_text = []
active_for_write_message_text = False
#----- add_InlineKeyboardButtons
text_url_button_list = []
textof = ''
urlof = ''
active_of_url = False
active_of_text = False
i1 = ''
i2 = ''
g_base1 = False
g_base2 = False
keyboardw: InlineKeyboardMarkup = None

# ---------------------def--------------------------------
def set_id(bot: telebot.TeleBot,message,list: list) -> str: 
    global active_for_set_id, messagestr_for_set_id, i

    if message.text == 'add who take message':
        bot.send_message(message.chat.id, 'from your \'contact\' or \'id\'')
        active_for_set_id = True
        print(active_for_set_id)

    elif messagestr_for_set_id != []:   
        if int(i.__len__()) == 2:
            for g in range(int(list.__len__())):
                list_id = list[g].split(',',4)
                user_id = list_id[1]
                print(f'list num {g} id: \'{user_id}\', chat id: \'{message.chat.id}\'')
                if message.chat.id == int(user_id):
                    bot.reply_to(message,'you have id for send, we replace this id')
                    list[g] = f'user chat id: ,{message.chat.id}, write to id: ,{i[1]}'
                    active_for_set_id = False
                    print(active_for_set_id)
                    print(list)
                    i = []
                    messagestr_for_set_id = []
                    return
            
            list.append(f'user chat id: ,{message.chat.id}, write to id: ,{i[1]}')
            print(int(i.__len__()))
            bot.reply_to(message,'add without error')
            active_for_set_id = False
            print(active_for_set_id)
            print(list)
            i = []
            messagestr_for_set_id = []
        else:
            bot.reply_to(message,'oh, sorry you don\'t right write your id, you need write: id: here id')
            i = []
            messagestr_for_set_id = []

    elif active_for_set_id == True:
        last = messagestr_for_set_id.append(message.text)
        print(last)
        i = messagestr_for_set_id[0].split(': ', 1)
        print(i)
    else:
        print(None)

def send_message(bot: telebot.TeleBot,message,list: list):
    active2 = True
    realy = ' '

    if message.text == 'send message':
        for g in range(int(list.__len__())):
            list_id = list[g].split(',',4)
            user_id = list_id[1]
            chat_send_id = list_id[3]
            print(f'list num {g} id: \'{user_id}\', chat id: \'{message.chat.id}\'')
            if message.chat.id == int(user_id):
                try:
                    bot.send_message(chat_id=chat_send_id,text=potion_funk(message), reply_markup=__reply_markup__(message))
                    bot.reply_to(message,'message send without error')
                    active2 = False
                except Exception as e:
                    bot.reply_to(message,f'we can\'t find chat to send message, Error {e}')
                    realy = ' realy '

        if active2:
            bot.reply_to(message,f'please give{realy}id to send')
    else:
        print('none')

def write_message_text(bot: telebot.TeleBot,message):
    global active_for_write_message_text, messagestr_for_write_message_text, text_to_send

    if message.text == 'add text message':
        bot.send_message(message.chat.id, 'wite text')
        active_for_write_message_text = True
        print(active_for_write_message_text)

    elif messagestr_for_write_message_text != []:   
        for g in range(int(text_to_send.__len__())):
                list_text = text_to_send[g].split(',',4)
                user_id = list_text[1]
                print(f'list num {g} id: \'{user_id}\', chat id: \'{message.chat.id}\'')
                if message.chat.id == int(user_id):
                    bot.reply_to(message,'you have text for send, we replace this text')
                    text_to_send[g] = f'user chat id: ,{message.chat.id}, text write: ,{message.text}'
                    print(active_for_set_id)
                    print(text_to_send)
                    return
        text_to_send.append(f'user chat id: ,{message.chat.id}, text write: ,{message.text}')
        bot.reply_to(message,'add without error')
        active_for_write_message_text = False
        messagestr_for_write_message_text = []

    elif active_for_write_message_text == True:
        messagestr_for_write_message_text.append(f'user chat id: ,{message.chat.id}, text write: ,{message.text}')
    else:
        print(None)

def potion_funk(message) -> str:
    global text_to_send

    for g in range(int(text_to_send.__len__())):
        list_text = text_to_send[g].split(',',4)
        user_id = list_text[1]
        print(f'list num {g} id: \'{user_id}\', chat id: \'{message.chat.id}\'')
        if message.chat.id == int(user_id):
            return list_text[3]

def test_message(bot: telebot.TeleBot,message):

    if message.text == 'test message':
        for g in range(int(text_to_send.__len__())):
            list_id = text_to_send[g].split(',',4)
            user_id = list_id[1]
            print(f'list num {g} id: \'{user_id}\', chat id: \'{message.chat.id}\'')
            if message.chat.id == int(user_id):
                try:
                    bot.send_message(chat_id=message.chat.id, text=potion_funk(message), reply_markup=__reply_markup__(message))
                    bot.reply_to(message,'message send without error')
                except Exception as e:
                    bot.reply_to(message,f'Error {e}')

def add_InlineKeyboardButtons(bot: telebot.TeleBot, message):
    global textof, urlof, active_of_text, active_of_url, text_url_button_list, i1, i2,g_base1,g_base2,keyboardw

    if message.text == 'add url button':
        bot.reply_to(message,'write text button: ')
        active_of_text = True
        print(active_of_text)
        
    elif textof != '' and urlof != '':
        print('ssssssssssssssssssssssss')

        if g_base1 and g_base2:
            text_url_button_list[i1] = f'user chat id: ,{message.chat.id}, url: ,{urlof}, text write: ,{textof}'
            textof = ''
            urlof = ''
            g_base1 = False
            g_base2 = False
            print('remove')
        else:
            keyboard = InlineKeyboardMarkup()
            for button in text_url_button_list:
                i = button.split(',',7)
                user_id1 = i[1]
                url1 = i[3]
                text_write = i[7]
                if message.chat.id == int(user_id1):
                    try:
                        button1 = InlineKeyboardButton(text=text_write, url=url1)
                        keyboard.add(button1)
                        keyboardw = keyboard
                        print(text_url_button_list)
                        print(keyboardw)
                        text_url_button_list.append(f'user chat id: ,{message.chat.id}, url: ,{urlof}, keyboard: ,{keyboardw}, text write: ,{textof}')
                        print(f'append: {text_url_button_list}')
                        bot.reply_to(message, 'add')
                    except Exception as e:
                        bot.reply_to(message, f'Error {e}')

            textof = ''
            urlof = ''

    elif active_of_text == True:
        print('start range')
        for g in range(int(text_url_button_list.__len__())):
            list_text = text_url_button_list[g].split(',',5)
            user_id = list_text[1]
            text = list_text[4]
            print('wedfsdsxz')
            if message.chat.id == int(user_id):
                bot.reply_to(message,'you have text for send, we replace this text')
                textof = message.text
                g_base1 = True
                active_of_text = False
                active_of_url = True
                i1 = g
                print('replace')
                return
            
        print('end()')
        textof = message.text
        bot.reply_to(message,'write url: ')
        print(f'write: {textof}')
        active_of_text = False
        active_of_url = True
        print(f'active of text{active_of_text} active of url {active_of_url}')

    elif active_of_url == True:
        print('s')
        for g in range(int(text_url_button_list.__len__())):
            list_text = text_url_button_list[g].split(',',5)
            user_id = list_text[1]
            url = list_text[3]
            if message.chat.id == int(user_id):
                bot.reply_to(message,'you have text for send, we replace this url')
                urlof = message.text
                g_base2 = True
                active_of_url = False
                i2 = g
                print('replace')
                return print('end')
        urlof = message.text
        print(f'write: {urlof}')
        active_of_url = False
        bot.reply_to(message,'all take without error')
        return True
    else:
        print(None)

def __reply_markup__(message):
    global keyboardw, text_url_button_list
    for g in range(int(text_url_button_list.__len__())):
        list_text = text_url_button_list[g].split(',',7)
        user_id = list_text[1]
        print('wedfsdsxz')
        if message.chat.id == int(user_id):
            print(f'Return {keyboardw}')
            return keyboardw
    print('return False')
    return False