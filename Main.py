import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


API_TOKEN = '6123092047:AAFxmv1W_c1W1fAmZzlvmDGluW17c-AtBsw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

"""
                                         Inline Keyboard Buttons
"""

inline_btn_1 = KeyboardButton('Ramazon Taqvim 📅', callback_data='button1')
inline_btn_2 = KeyboardButton('Duolar 🤲', callback_data='button2')
inline_btn_3 = KeyboardButton('Salovatlar 📿', callback_data='button3')
inline_btn_4 = KeyboardButton('Namoz kitobi 📕', callback_data='button4')
inline_kb1 = ReplyKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3).add(inline_btn_4)

"""
                                            Callback Data querys
"""
@dp.message_handler(text='Ramazon Taqvim 📅')
async def send_ramadan_takvim(message: types.Message):
    rasm = open('ramadan_Calendar.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=rasm)
@dp.message_handler(text='Duolar 🤲')
async def send_duo(message: types.Message):
    await message.reply("<b>Saharlik duosi\n\nNavaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi taʼaalaa Allohu akbar.\n \nIftorlik duosi\n\nAllohumma laka sumtu va bika aamantu va aʼlayka tavakkaltu va aʼlaa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.</b>", parse_mode="HTML")

@dp.message_handler(text='Salovatlar 📿')
async def send_salovat(message: types.Message):
    await message.reply("<b>Eng go'zal salovatlardan biri 👇👇\n\nAllohumma Solli A'la Sayyidina Muhammadin Va A'la Sayyidina Muhammadin  Va A'la Ali Sayyidina Muhammad</b>", parse_mode="HTML")

@dp.message_handler(text='Namoz kitobi 📕')
async def send_salovat(message: types.Message):
    file_namaz = open('namaz kitobi.rar', 'rb')
    await bot.send_document(message.chat.id, document=file_namaz)

"""
                                         Messages it's /start and /help commands 
"""

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("<b>Assalomu alaykum {} !\n\nRamazon oyi muborak bo'lsin !\n\nKerakli bo'limni tanlang 👇👇</b>".format(message.from_user.full_name), parse_mode="HTML", reply_markup=inline_kb1,)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("<b>Biz sizga qanday\n\nQanday yordam ko'rsatishimiz\n\nMumkin !\n\nSavol yoki takliflar bo'lsa\n\n Adminga Murojaat eting !\n\nAdmin: @adminramadan2023</b>", parse_mode="HTML")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)