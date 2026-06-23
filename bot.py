import discord
import requests
import time

import os
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1518970034175742184

client = discord.Client(intents=discord.Intents.default())

last_post = None

import discord
import requests
import os
import asyncio
import xml.etree.ElementTree as ET

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1518970034175742184

client = discord.Client(intents=discord.Intents.default())

last_post = None


def get_latest_post():
    url = "https://twitrss.me/twitter_user_to_rss/?user=95rn16"
    res = requests.get(url)

    if res.status_code != 200:
        return None, None

    root = ET.fromstring(res.text)
    item = root.find(".//item")

    if item is None:
        return None, None

    title = item.find("title").text
    link = item.find("link").text

    return title, link


async def check_posts():
    global last_post

    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        try:
            tweet, link = get_latest_post()

            if tweet and tweet != last_post:
                last_post = tweet
                await channel.send(f"🚨 新貼文\n\n{tweet}\n\n{link}")

        except Exception as e:
            print("錯誤:", e)

        await asyncio.sleep(60)


@client.event
async def on_ready():
    print("Bot 已上線")
    client.loop.create_task(check_posts())


client.run(TOKEN)
