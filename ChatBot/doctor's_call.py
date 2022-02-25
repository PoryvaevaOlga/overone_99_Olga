import telebot
from telebot import types

# 5125202741:AAFM1UFvsO3dk01ig_x4qeqH1Qv5aHFew-8

name = ''
surname = ''
age = 0
address = ''
complaints = ''

bot = telebot.TeleBot("5125202741:AAFM1UFvsO3dk01ig_x4qeqH1Qv5aHFew-8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Приветствую Вас!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, f'{message.text} дорогой друг')
	bot.send_message(message.from_user.id, 'Как тебя зовут?')
	bot.register_next_step_handler(message, reg_name)

def reg_name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, 'Ваша фамилия ?')
	bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
	global surname
	surname = message.text
	bot.send_message(message.from_user.id, 'Ваш возраст ?')
	bot.register_next_step_handler(message, reg_age)

def reg_age(message):
	global age
	age = message.text
	try:
		age = int(message.text)
	except Exception:
		bot.send_message(message.from_user.id, 'Введите цифрами')
		return 	bot.register_next_step_handler(message, reg_age)
	bot.send_message(message.from_user.id, 'Ваш адрес?')
	bot.register_next_step_handler(message, reg_address)

def reg_address(message):
	global address
	address = message.text
	bot.send_message(message.from_user.id, 'Ваши жалобы?')
	bot.register_next_step_handler(message, reg_complaints)

def reg_complaints(message):
	global complaints
	complaints = message.text
	keyboard = types.InlineKeyboardMarkup()
	key_yes = types.InlineKeyboardButton(text='да', callback_data='yes')
	keyboard.add(key_yes)
	key_no = types.InlineKeyboardButton(text='нет', callback_data='no')
	keyboard.add(key_no)
	quistion = 'вам ' + str(age) + ' лет? ' \
			   '\nи Вас зовут: ' + name + '' \
'' + surname + '\nваш адрес: ' + address +\
			   '\nваши жалобы: ' + complaints + '?'
	bot.send_message(message.from_user.id, text = quistion, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def	callback_worker(call):
	if call.data == 'yes':
		bot.send_message(call.message.chat.id, 'обращение принято')
	elif call.data == 'no':
		bot.send_message(call.message.chat.id, 'данные введены неверно. повторите ')
		bot.send_message(call.message.chat.id, 'Как тебя зовут?')
		bot.register_next_step_handler(call.message, reg_name)

# bot.infinity_polling()
bot.polling()