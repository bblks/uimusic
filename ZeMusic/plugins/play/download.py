import os
import requests
import config
import aiohttp
import aiofiles
from ZeMusic.platforms.Youtube import cookie_txt_file

import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from youtube_search import YoutubeSearch

from ZeMusic import app
from ZeMusic.plugins.play.filters import command

def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)
channel = "ngd_1"              
lnk = config.CHANNEL_LINK
Nem = config.BOT_NAME + " ابحث"

@app.on_message(filters.regex(r"^(بحث)"))
async def searcher(_, message: Message):
    chat_id = message.chat.id
    wait = await message.reply_text("Processing...")
    text = message.text.split(" ", 1)[1]
    try: search = Search(text)
    except: return await app.edit_message_text(
                chat_id=chat_id,
                message_id=wait.id, 
                text="An error occurred or no results were found."
            )
    result = search.results[0]
    info = result.vid_info["videoDetails"]
    vid_id = info["videoId"]
    title = info["title"]
    author = info["author"]
    length = info["lengthSeconds"]
    views = info["viewCount"]
    thumbnail = info["thumbnail"]["thumbnails"][-1]["url"]
    caption = f"- title: {title}\n- author: {author}\n- duration: {length}sec.\n- views: {views}"
    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("- التالي -", callback_data=f"next_{text}_0"),
        ],
        [
            InlineKeyboardButton("- Watch In YouTube -", url=f"https://www.youtube.com/watch?v={vid_id}"),
            InlineKeyboardButton("- Download Thumbnail -", url=thumbnail)
        ],
        [
            InlineKeyboardButton("- Dev ⛄️ -", url="Z_l_7.t.me")
        ]
    ])
    await message.reply_photo(
        photo = thumbnail, 
        caption = caption,
        reply_to_message_id = message.id,
        reply_markup = markup
    )
    await app.delete_messages(chat_id, wait.id)


@app.on_callback_query(filters.regex(r"^(next|back)"))
async def returner(_, callback: CallbackQuery):
    await app.answer_callback_query(callback.id, "- Wait a few seconds, please.")
    chat_id = callback.message.chat.id
    data = callback.data.split("_")[1:]
    text = data[0]
    index = int(data[1]) + 1 if callback.data.startswith("next") else int(data[1]) - 1
    search = Search(text)
    result = search.results[index]
    info = result.vid_info["videoDetails"]
    title = info["title"]
    author = info["author"]
    length = info["lengthSeconds"]
    views = info["viewCount"]
    thumbnail = info["thumbnail"]["thumbnails"][-1]["url"]
    caption = f"- title: {title}\n- author: {author}\n- duration: {length}sec.\n- views: {views}"
    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "- التالي -" if index < len(search.results) else "- النهايه -", 
                callback_data=f"next_{text}_{index}" if index < len(search.results) else "theEnd"),
            InlineKeyboardButton(
                "- العوده -" if index != 0 else "- البدايه -",
                callback_data=f"back_{text}_{index}" if index != 0 else "theStart")
        ],
        [
            InlineKeyboardButton("- Watch In YouTube -", url=f"https://www.youtube.com/watch?v={info['videoId']}"),
            InlineKeyboardButton("- Download Thumbnail -", url=thumbnail)
        ],
        [
            InlineKeyboardButton("- Dev ⛄️ -", url="Z_l_7.t.me")
        ]
    ])
    await app.edit_message_media(
        chat_id=chat_id,
        message_id=callback.message.id, 
        media=InputMediaPhoto(thumbnail, caption=caption),
        reply_markup=markup
    )

def main():
    print("Hello!")
    app.run()

if __name__=="__main__": main()
# 𝗪𝗥𝗜𝗧𝗧𝗘𝗡 𝗕𝗬 : @Z_l_7
# 𝗦𝗢𝗨𝗥𝗖𝗘 : @NGD_1
