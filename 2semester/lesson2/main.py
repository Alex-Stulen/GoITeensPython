# from googletrans import Translator
#
# translator = Translator()
#
# file = open("text.txt", mode="r")
# lines = file.readlines()
# file.close()
#
# for index in range(len(lines)):
#     lines[index] = lines[index].strip()
#
# from_lang = "en"
# to_lang = "uk"
#
# result = translator.translate(lines, src=from_lang, dest=to_lang)
#
# for trans in result:
#     print(f"{trans.origin} -> {trans.text}")


import requests

url = "https://api.telegram.org/bot6202350822:AAEb8Iv2whI8frRzhIUcpLPQCU26K-i2Wp8/sendMessage"

request_body = {
    "text": "Hello from Python",
    "chat_id": 803678440
}

response = requests.get(url=url, params=request_body)

print(response.json())
