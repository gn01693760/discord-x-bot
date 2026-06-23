import discord
import requests
import time

import os
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1518970034175742184

client = discord.Client(intents=discord.Intents.default())

last_post = None

import snscrape.modules.twitter as sntwitter

def get_latest_post():
    for tweet in sntwitter.TwitterUserScraper("95rn16").get_items():
        return tweet.content, tweet.url

@client.event
async def on_ready():
    global last_post
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

        time.sleep(60)

client.run(TOKEN)
