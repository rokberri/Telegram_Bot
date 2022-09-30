import telebot
import requests
from bs4 import BeautifulSoup

# FINALS
# API_TOKEN = '5662360252:AAFuHDxBwgGPL0QobOmK3fHVcvt_S7W-Gqc'
URL = "http://www.consultant.ru/document/cons_doc_LAW_10699/"
# bot = telebot.TeleBot(API_TOKEN)


# print(requests.get(URL).status_code) #check if it's work
# print(requests.get(URL).text) #get full html text

# ---------------------------------------------------------------------------
# скрипт для обновления бд на локалке
# q = requests.get(URL)
# result = q.content
#
# soup = BeautifulSoup(result, 'lxml')
# titles = soup.find(class_='document-page__toc').find_all('a')
#
# title_href = []
#
# for title in titles:
#     href = title.get('href')
#     text = title.text
#     title_href.append(f'{href} --- {text}')
#
# with open('titles_url_list.txt', 'w') as file:
#     for line in title_href:
#         file.write(f'{line}\n')

# ---------------------------------------------------------------------------

# создать словарь, ключ - название статьи и краткое описание, значение - ссылка
# нужно будет внести изменения в схему т.к. обновляем бд и не каждый раз докалебываем сайт

# utdtycutguhiok
# nnin




# @bot.message_handler(content_types=['/start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, я бот Юрик')
#
#
#
# bot.polling(none_stop=True, interval=0)