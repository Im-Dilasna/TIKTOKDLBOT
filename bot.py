"""
MIT License

Copyright (c) 2022 SLNinjaTeamBot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# Powered By SLNinjaTeam

import os 

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
import requests
from requests import get

bot = Client(
   "Tiktok Downloader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)
@bot.on_message(filters.command("start"))
async def start(client, message):
       await bot.send_message(
               chat_id=message.chat.id,
               text="""<b>💁‍♂️ Hey There, I'm TikTokDL Bot\nI can Download TikTok Video Without Watermark\n\n🔥 Help :</b>\n/tiktok [Tiktok Url]</b>\n\n<b>🚀 Powered By :</b> @SLNinjaTeam """,   
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Channel", url="https://t.me/SLninjaTeamchannel")]],
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@bot.on_message(filters.command("tiktok"))
async def make_logo(_, message):
    imgcaption = f"""
☘️**TikTok Video Upload Successfully**
◇───────────────◇
🔥 **Created by** : @SNTTikTokDLBot
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : SNT™ 🇱🇰
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("💁‍♂️ **Please give a url to Download Video**")
    m = await message.reply_text("**🚀 Downloading..**")
    url = message.text.split(None, 1)[1]
    video = get(f"https://single-developers.up.railway.app/tiktok?url={url}").history[1].url
    await m.edit("📤 **Uploading ...**")
    await bot.send_video(message.chat.id, video=video, caption=imgcaption.format(message.from_user.mention))
    await m.delete()

bot.run()