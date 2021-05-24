# Made with python3
# (C) @FayasNoushad
# Copyright permission under GNU General Public License v3.0
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Telegraph-Uploader-Bot/blob/main/LICENSE

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file

FayasNoushad = Client(
        "Telegraph Uploader Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"]
)

START_TEXT = """<b>Hai,

I'm a simple Telegraph Uploader bot💯

I can convert gif, image or video(Mp4only) into telegra.ph links

Click help for more details...

You must subscribe our channel in order to use me😇</b>"""
HELP_TEXT = """<b>Hey.. It's not that complicated

Follow These steps..

🌀 Send any Image, Gif or Video(Mp4 oNly) below 5MB

🌀 Wait for the link to get generated

NOTE : Currently I don't support text to telegraph</b>"""
ABOUT_TEXT = """⭕️<b>My Name : CoderZ Image Editor</b>

⭕️<b>Language :</b> <code>Python3</code>

⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a>

⭕️<b>Creator :</b> <a href='https://telegram.me/MaxxcoderZ'>Maxx ⚡</a>

⭕<b>Source Code :</b> 👉 <a href='https://github.com/CW4RR10R/Image-UploadBot'>click here</a>"""
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HELP', callback_data='help'),
        InlineKeyboardButton('ABOUT', callback_data='about'),
        InlineKeyboardButton('⭕ JOIN OUR CHANNEL ⭕', url='https://telegram.me/CODERZHEX')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME', callback_data='home'),
        InlineKeyboardButton('ABOUT', callback_data='about'),
        InlineKeyboardButton('⭕ JOIN OUR CHANNEL ⭕', url='https://telegram.me/CODERZHEX')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⭕ CHANNEL ⭕', url='https://telegram.me/CODERZHEX'),
        InlineKeyboardButton('⭕ SUPPORT ⭕', url='https://telegram.me/CODERZSUPPORT')
        ],[
        InlineKeyboardButton('HOME', callback_data='home'),
        InlineKeyboardButton('HELP', callback_data='help'),
        InlineKeyboardButton('CLOSE', callback_data='close')
        ]]
    )

@FayasNoushad.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
    

@FayasNoushad.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@FayasNoushad.on_message(filters.media & filters.private)
async def getmedia(bot, update):
    medianame = "./DOWNLOADS/" + "FayasNoushad/FnTelegraphBot"
    message = await update.reply_message(
        text="<code>Downloading to My Server ...</code>",
        disable_web_page_preview=True
    )
    await bot.download_media(
        message=update,
        file_name=medianame
    )
    await message.edit_text(
        text="<code>Downloading Completed. Now I am Uploading to telegra.ph Link ...</code>"
    )
    try:
        response = upload_file(medianame)
    except Exception as error:
        print(error)
        text=f"Error :- <code>{error}</code>"
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('⭕ SUPPORT ⭕', url='https://telegram.me/coderzsupport')
            ]]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
    text=f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n<b>Join :-</b> @FayasNoushad"
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Open Link 🔓", url=f"https://telegra.ph{response[0]}"),
        InlineKeyboardButton(text="Share Link ♐", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}"),
        ],[
        InlineKeyboardButton(text="⭕ Join our Channel ⭕", url="https://telegram.me/CoderzHEX")
        ]]
    )
    await message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    try:
        os.remove(medianame)
    except:
        pass

FayasNoushad.run()
