import requests
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

url = "https://minfin.com.ua/currency/crypto/"
header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': "utf-8",
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent':  # YOUR USER AGENT
}
r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, "html.parser")
div = soup.find("div", class_="sc-ny2dqf-3 eMhSII").find_all("a", class_="sc-18qu8it-2 hmBaVo")
a_list = []
value_list = []
for i in div:
    link = "https://minfin.com.ua/" + i.get("href")
    span = i.find("a")
    value_list.append(span.text)
    a_list.append(link)


TOKEN = "5652375388:AAHMtFlGGGd5y6OsencCOkamCd0Ofvn7oMw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def get(message: types.Message):
        count = 0
        for i in a_list:
            await message.answer(f"{value_list[count]} - {i}")
            count += 1


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
