import asyncio
from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker, emoji

MENTION = "{}"  
MESSAGE = "{} Hello Welcome To My Name Is TOKYO BOT, I Can Provide Movies/Series In This Group.
Just Type The Actual Name Of The Movie/Series.
You Will Get The Movie/Series If You Write Correct Spelling.
If You Don't Get The Movie/Series It Is Sure That You Have Written Incorrect Spelling Or Your Requested Movie/Series Does Not Exit In My Database {}!" 

@LuciferMoringstar_Robot.on_message(Worker.new_chat_members)
async def welcome(client, message):

    new_members = [MENTION.format(message.from_user.mention) for i in message.new_chat_members]

    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))

    dell=await message.reply_text(text, disable_web_page_preview=True)
    await asyncio.sleep(1000)
    await dell.delete()
