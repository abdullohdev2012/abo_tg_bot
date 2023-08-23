import logging
from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton
from aiogram import Bot ,Dispatcher ,executor,types
from tugmalar import *


logging.basicConfig(level=logging.INFO)

BOT_TOKEN ="6013819147:AAGK3KpVKYz0bPEIG9R4xEpmMVU_nY86SfI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start","menu"])
async def bot_start_handler(message :types.Message):
    await message.answer("Assalomu aleykum ", reply_markup=bosh_menu)



  

@dp.message_handler(text="orqaga")
async def bot_start_handler(message:types.Message) :
    await message.answer("mana",reply_markup=bosh_menu)    


@dp.message_handler(text="14500 so'mlik pechenyalar") 
async def bot_start_handler(message:types.Message) :
    await message.answer("mana",reply_markup=birinchi_menu)  



@dp.message_handler(text="19500 so'mlik pechenyalar") 
async def bot_start_handler(message:types.Message) :
    await message.answer("mana",reply_markup=ikkinchi_menu)  

@dp.message_handler(text="mini ko'rn") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("mini_korn2.jpg")
    await message.answer_photo(photo=rasm ,caption="""mini ko'rn :
        massa :4 kg 
        narxi :14500""")


@dp.message_handler(text="18700 so'mlik pechenyalar") 
async def bot_start_handler(message:types.Message) :
    await message.answer("mana",reply_markup=uchinchi_menu)

    
@dp.message_handler(text="mini yubileyniy") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("mini_yub2.jpg")
    await message.answer_photo(photo=rasm ,caption="""mini yubileyniy :
        massa :4 kg 
        narxi :14500""")

@dp.message_handler(text="olma") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("olma2.jpg")
    await message.answer_photo(photo=rasm ,caption="""olma :
        massa :4 kg 
        narxi :14500""")

@dp.message_handler(text="neskafe") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("neskafe2.jpg")
    await message.answer_photo(photo=rasm ,caption="""neskafe :
        massa :3 kg 
        narxi :14500""")
@dp.message_handler(text="abo") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("abo2.jpg")
    await message.answer_photo(photo=rasm ,caption="""abo :
        massa :3 kg 
        narxi :14500""")

@dp.message_handler(text="davr") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("davr2.jpg")
    await message.answer_photo(photo=rasm ,caption="""davr :
        massa :3 kg 
        narxi :14500""")        

@dp.message_handler(text="abo kvadrat") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("abokub2.jpg")
    await message.answer_photo(photo=rasm ,caption="""abo kvedrat  :
        massa :3 kg 
        narxi :14500""")

@dp.message_handler(text="medved") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("medved.jpg")
    await message.answer_photo(photo=rasm ,caption="""medved :
        massa :3 kg 
        narxi :14500""")    


@dp.message_handler(text="masha") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("masha_2.jpg")
    await message.answer_photo(photo=rasm ,caption="""masha :
        massa :3 kg 
        narxi :14500""") 
    
@dp.message_handler(text="nejniy") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("nejniy.jpg")
    await message.answer_photo(photo=rasm ,caption="""nejniy :
        massa :3 kg 
        narxi :14500""")     



@dp.message_handler(text="makka joxori") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("makka_joxori.jpg")
    await message.answer_photo(photo=rasm ,caption="""makka joxori:
        massa :3 kg 
        narxi :14500""") 
    
@dp.message_handler(text="kapalak") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("kapale2.jpg")
    await message.answer_photo(photo=rasm ,caption="""kapalak :
        massa :3 kg 
        narxi :14500""") 
    

@dp.message_handler(text="oltin diyor") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("oltindiyor2.jpg")
    await message.answer_photo(photo=rasm ,caption="""makka joxori:
        massa :3 kg 
        narxi :14500""") 
    
@dp.message_handler(text="toplonka") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("toplonka2.jpg")
    await message.answer_photo(photo=rasm ,caption="""kapalak :
        massa :3 kg 
        narxi :14500""")    


@dp.message_handler(text="alonka") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("alyonka.jpg")
    await message.answer_photo(photo=rasm ,caption="""alonka:
        massa :3 kg 
        narxi :18700""") 
    
@dp.message_handler(text="padushka") 
async def bot_start_handler(message:types.Message) :
    rasm = types.InputFile("podushka2.jpg")
    await message.answer_photo(photo=rasm ,caption="""podushka :
        massa :3 kg 
        narxi :19500""") 


if __name__ == "__main__":
    executor.start_polling(dp)



   