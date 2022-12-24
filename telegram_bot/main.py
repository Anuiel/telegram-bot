from create_bot import bot, dp
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram.types.input_file import InputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import sys

from pathlib import Path
import os, hashlib

keyboards = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton("/start")
b2 = KeyboardButton("/text")
b3 = KeyboardButton("/gif")
b4 = KeyboardButton("/sticker")
b5 = KeyboardButton("/photo")

keyboards.row(b2, b3).row(b4, b5)

@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await message.answer("This bot sends Masyunya releated stuff into your dm's!", reply_markup=keyboards)


@dp.message_handler(commands=["text"])
async def send_text(message: types.Message):
    await message.reply("God, I love Masyunya!")


@dp.message_handler(commands=["photo"])
async def send_photo(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=open(f"./data/photo/1.jpg", 'rb'))

@dp.message_handler(commands=["sticker"])
async def send_photo(message: types.Message):
    await bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEGkYtjgr8BqQFeLToN4n5MSVLRvdbh_gACOhgAApOSEUqJPbIB_y7HkisE")

@dp.message_handler(commands=["gif"])
async def send_photo(message: types.Message):
    await bot.send_animation(message.from_user.id, open(f"./data/gif/1.gif", 'rb'), None, "Text")


executor.start_polling(dp, skip_updates=True)