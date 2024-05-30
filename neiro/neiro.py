import requests
import base64
import time
from random import randint
# from aiogram import Bot, types, executor, Dispatcher
#
# API='7282364928:AAHn2eFf9y5nX0tPc-PWnuHiWcd1aUJyV5k'
# bot = Bot(token=API)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands= 'start')
# async def start(message: types.Message):
#     await message.answer("Барев я нейрон")


def generate_image(prompt_text):
    prompt = {
        "modelUri": "art://b1guhm2737ndflt1edic/yandex-art/latest",
        "generationOptions": {
          "seed": randint(10000,2000000000)
        },
        "messages": [
          {
            "weight": 1,
            "text": prompt_text
          }
        ]
        }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"

    headers = {
             "Content-Type": "application/json",
             "Authorization": "Api-Key AQVN1Rp3exxihHr1hDz34NMWyqRcz3hNf5_nml7E"
         }

    response = requests.post(url=url, headers=headers,json=prompt)
    result = response.json()
    print(result)


    operation_id = result['id']

    operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"

    while True:
        operation_response = requests.get(url= operation_url, headers=headers)
        operation_result = operation_response.json()
        if 'response' in operation_result:
            image_base64 = operation_result['response']['image']
            image_data = base64.b64decode(image_base64)
            return image_data
        else:
            print('Ожидайте изображение не готово')
            time.sleep(1)


