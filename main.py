from aiogram import Bot, types, executor, Dispatcher
from neiro.neiro import generate_image
from neiro.neiro_assistant import get_response
from neiro.neiro_consult import get_sovet

API='7282364928:AAHn2eFf9y5nX0tPc-PWnuHiWcd1aUJyV5k'
bot = Bot(token=API)
dp = Dispatcher(bot)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer("Барев я нейрон")

@dp.message_handler(commands='sovet')
async def analize_message(message:types.Message):
    user = message.get_args()
    response_text = await get_sovet(user)
    await message.answer(response_text)



@dp.message_handler(commands='img')
async def handle_message(message: types.Message):
    user = message.get_args()
    response_text = await get_response(user)
    user_text = response_text
    await message.reply(f"Вот твой улучшенный промпт: {user_text}")
    print(user_text)
    await message.reply('Идет генерация изображения, жди')

    try:
        image_data = generate_image(user_text)
        await message.reply_photo(photo= image_data)
    except Exception as e:
        await message.reply(f"Произошла ошибка {e}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)