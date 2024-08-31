import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID
import config

@app.on_message(
  command(["المبرمج","مبرمج السورس","مبرمج","مطور السورس"])
)
async def huhh(client: Client, message: Message):
    dev_id = 7085943284
    dev = await client.get_users(dev_id)
    name = dev.first_name
    usrnam = dev.username
    
    await app.download_media(dev.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
   
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b> 𝙽𝙰𝙼𝙴 :</b> <a href='https://t.me/{usrnam}'>{name}</a>\n\n<b> 𝚄𝚂𝙴𝚁 :</b> {usrnam}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         name, url=f"https://t.me/{usrnam}"), 
                 ],[
                   InlineKeyboardButton(
                        "𝐬𝐨𝐮𝐫𝐜𝐞 𝐚𝐥𝐢𝐜𝐞", url=f"https://t.me/ngd_1"),
                ],

            ]

        ),

    )
