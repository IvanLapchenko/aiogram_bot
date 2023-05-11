import random
import sys
from loader import dp
from aiogram import types
from .service.parser import get_four_headers_and_links, get_article_by_its_link, get_all_links_from_page
from bot.keyboards.default import reply_markup as reply
from bot.keyboards.inline import economic_reply_markup, politic_reply_markup

sys.path.insert(0, '/bot')

global links


@dp.message_handler(state=None, commands='whattoread')
async def bot_echo(message: types.Message):
    await message.answer('Choose topic', reply_markup=reply)


@dp.message_handler(state=None, text='Economic news')
async def handle_economic_news(message: types.Message):
    global links
    headers, links = get_four_headers_and_links('https://www.epravda.com.ua/news/')
    await message.answer('Choose the article: \n'
                         f'1. {headers[0]}\n'
                         f'2. {headers[1]}\n'
                         f'3. {headers[2]}\n'
                         f'4. {headers[3]}\n', reply_markup=economic_reply_markup)


@dp.message_handler(state=None, text='EU news')
async def handle_economic_news(message: types.Message):
    global links
    headers, links = get_four_headers_and_links('https://www.eurointegration.com.ua/news/')
    await message.answer('Choose the article: \n'
                         f'1. {headers[0]}\n'
                         f'2. {headers[1]}\n'
                         f'3. {headers[2]}\n'
                         f'4. {headers[3]}\n', reply_markup=politic_reply_markup)


@dp.message_handler(state=None, commands='randomtopic')
async def bot_echo(message: types.Message):
    link = 'https://www.pravda.com.ua/news/'
    articles = get_all_links_from_page(link)
    rand_link = random.choice(articles)
    article_text = get_article_by_its_link(rand_link)
    await message.answer(article_text)


@dp.callback_query_handler(text_contains='p')
async def second_step(call: types.CallbackQuery):
    global links
    index = int(call.data[1])
    link = links[index]
    article_text = get_article_by_its_link(link)
    await call.message.answer(article_text)


@dp.callback_query_handler(text_contains='e')
async def second_step(call: types.CallbackQuery):
    global links
    index = int(call.data[1])
    link = links[index]
    article_text = get_article_by_its_link(link)
    await call.message.answer(article_text)
