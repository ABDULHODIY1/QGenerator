# from aiogram import types ,executor,Dispatcher, Bot

# API_TOKEN=''
# bo=Bot(token=API_TOKEN)
# dp=Dispatcher(bo)

# @dp.message_handler()
# async def startbot(message:types.Message):
#     await message.answer(text=f'Hi{message.from_user.username}!!!')
#     await message.answer(text='Welcome to this bot')


# if '__name__' == '__main__':
#     executor.start_polling(dp,skip_updates=True)

import os
import json
i=json.loads(open("words.json").read())
for i in i["klo"]:
    for i in i["patterns"]:
        print(f"""
              {i}
              """)