import asyncio
from ZeMusic import app
from config import OWNER_ID
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
import config

$question = str_replace("همس ","",$text);
if($text == "همس ".$question){
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://hmss.store/api/chat.php?text=".urlencode($question));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT,30);
$result = curl_exec($ch);
curl_close($ch);
bot('Sendmessage',[
'chat_id'=>$chat_id,
'text'=>$result,
'reply_to_message_id'=>$message_id,
]);
}
