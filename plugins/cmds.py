#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DforDarkAngel
# @DX_Botz

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton ,CallbackQuery
import os, shutil
from config import Config
from telegraph import upload_file
import logging
from translation import Translation

@Client.on_message(filters.command("start"))
async def start(bot, update):
    buttons = [[
        InlineKeyboardButton('βοΈ Help', callback_data='help_btn'),
        InlineKeyboardButton('Support Group π', url='https://t.me/Dx_Support')
        ],[
        InlineKeyboardButton('πΈ Source Code', url='https://github.com/Jijinr/TGraph-Bot'),
        InlineKeyboardButton('Close π', callback_data='cancel_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        reply_to_message_id=update.message_id
    )
    
@Client.on_message(filters.command(["help"]))
async def help_user(bot, update):
    #logger.info(update)
    buttons = [[
        InlineKeyboardButton('π Support Group', url='https://t.me/Dx_Support'),
        InlineKeyboardButton('Update Channel π', url='https://t.me/DX_Botz')
        ],[
        InlineKeyboardButton('β»οΈShare', url='tg://msg?text=**Hey%20Broh**%F0%9F%A5%B0%2C%0A__This%20Bot%20Generate%20Telegraph%20Link__%F0%9F%94%A5%0A%0A**Bot%20Link**%20%3A-%20%40TGraphDXBot'),
        InlineKeyboardButton('Close π', callback_data='cancel_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        reply_to_message_id=update.message_id,
        parse_mode="html")
        
@Client.on_message(filters.command(["about"]))
async def get_me_info(bot, update):
    #logger.info(update)
    buttons = [[
        InlineKeyboardButton('πΈ Source code', url='https://github.com/Jijinr/TGraph-Bot'),
        InlineKeyboardButton('Close π', callback_data='cancel_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )