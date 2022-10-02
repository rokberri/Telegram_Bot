import string

import telebot
import requests
from bs4 import BeautifulSoup

# FINALS
URL = "http://www.consultant.ru/document/cons_doc_LAW_10699/"
titles_and_hrefs = {}


# print(requests.get(URL).status_code) #check if it's work
# print(requests.get(URL).text) #get full html text

# ---------------------------------------------------------------------------
# скрипт для обновления бд на локалке
def update_data_base():
    q = requests.get(URL)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')
    titles = soup.find(class_='document-page__toc').find_all('a')

    title_href = []

    for title in titles:
        href = title.get('href')
        text = title.text
        titles_and_hrefs[text] = href
        title_href.append(f'{href} --- {text}')

    with open('titles_url_list.txt', 'w') as file:
        for line in title_href:
            file.write(f'{line}\n')


# ---------------------------------------------------------------------------

# запись из файла в словарь
def create_dictationary():
    with open('titles_url_list.txt', 'r') as file:
        for line in file:
            splited_line = line.split('---')
            titles_and_hrefs[splited_line[1]] = (splited_line[0])


# поиск сообщения пользователя по ключам
def search_for(text, source):
    text = text.replace('/', '')
    list = []
    keys = source.keys()
    for key in keys:
        if key.find(text) != -1:
            list.append(key)
            print(list)
    return list


def telegram_bot():

    API_TOKEN = '5662360252:AAFuHDxBwgGPL0QobOmK3fHVcvt_S7W-Gqc'

    bot = telebot.TeleBot(API_TOKEN)

    # @bot.message_handler(commands=["start"])
    # def start_bot(message):
    #     bot.send_message(message.chat.id, 'Привет, я бот Юрик. Напиши мне номер статьи или ключевые слова и я попробую найти её')

    @bot.message_handler(commands=["46"])
    def find_title(message):
        list = search_for(message.text, titles_and_hrefs)
        bot.send_message(message.chat.id, "Searching...")
        print(list)
        for item in list:
            bot.send_message(message.chat.id, f'Вот что мне удалось найти: {item}\n{titles_and_hrefs.get(item)}\n')

    bot.polling()


def main():
    create_dictationary()
    print(search_for("45", titles_and_hrefs))


if __name__ == '__main__':
    # main()
    telegram_bot()
