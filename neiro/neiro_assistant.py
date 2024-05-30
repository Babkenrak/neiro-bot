import requests


async def get_response(message_text):
    prompt = {
        "modelUri": "gpt://b1gilp5v7bggj2ambvvp/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0,
            "maxTokens": 2000
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты - нейронная сеть, которая может улучшить запрос от пользователя, он передает тебе запрос, ты его улучшаешь в единичном формате и передаешь в нейронную сеть для генерации картинки"
            },
            {
            "role": "user",
            "text": message_text
            }
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-key AQVN0rHrwwPl2GzpROehfgY7EgK7ZQtkH9n34ayG"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    return result['result']['alternatives'][0]['message']['text']

