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
import time
import xml.etree.ElementTree as ET
import asyncio

last_post = None

async def check_posts():
    global last_post

    await client.wait_until_ready()

    while not client.is_closed():
        tweet, link = get_latest_post()

        if tweet and tweet != last_post:
            last_post = tweet

            channel = client.get_channel(YOUR_CHANNEL_ID)
            await channel.send(f"{tweet}\n{link}")

        await asyncio.sleep(60)

def get_latest_post():
    url = "https://twitrss.me/twitter_user_to_rss/?user=95rn16"
    res = requests.get(url)
    
    if res.status_code != 200:
        return None, None

    import xml.etree.ElementTree as ET
    root = ET.fromstring(res.text)

    item = root.find(".//item")
    title = item.find("title").text
    link = item.find("link").text

    return title, link
    
def get_latest_post():
    for tweet in sntwitter.TwitterUserScraper("95rn16").get_items():
        return tweet.content, tweet.url

@client.event
async def on_ready():
    print("Bot 已上線")

    channel = client.get_channel(CHANNEL_ID)

    while True:
        try:
            tweet, link = get_latest_post()

            if tweet != last_post:
                last_post = tweet

                await channel.send(
                    f"🚨 新貼文\n\n{tweet}\n\n{link}"
                )

        except Exception as e:
            print("錯誤:", e)

 await asyncio.sleep(60)

client.loop.create_task(check_posts())
client.run(TOKEN)
