""" A simple Discord bot made to reply to exclamation points.
    TODO: Add time based reminders to different events, like due dates """
import os
from datetime import datetime, time, timedelta
import asyncio

import discord
from discord.ext import commands, tasks
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))
CHANNEL = int(os.getenv('DISCORD_CHANNEL'))

intents = discord.Intents.all()

bot = commands.Bot(command_prefix= '.', intents=intents)
WHEN = datetime(2022, 3, 4, 22, 0, 0) #10:00.00pm
print(f'Original WHEN: {WHEN}')

async def turnin_reminder():
    """ Fires the weekly reminder in defined channel """
    await bot.wait_until_ready()
    channel = bot.get_guild(GUILD).get_channel(CHANNEL)
    await channel.send("Do your weekly review!")

@tasks.loop(minutes=30)
async def background_keeper():
    """ Station keeping function, checks if time to fire  """
    global WHEN

    now = datetime.now()
    FRIDAY = 4
    if now >= WHEN:
        if now.weekday() == FRIDAY:
            print("Valid Weekday")
            await turnin_reminder()
        WHEN =  WHEN + timedelta(days=7)
        print(f'New WHEN: {WHEN}')

@bot.event
async def on_ready():
    """Waits for bot to initialize, then prints bot & guild info"""
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))
    print('Bot is ready to be used')

    background_keeper.start()
    for guild in bot.guilds:
        print(f'Guild name: {guild}\nGuild ID: {guild.id}\n')
        print('Members:')
        for member in guild.members:
            print(f'- {member}')

@bot.event
async def on_message(message):
    """Message response handler"""

    if message.author == bot.user:
        return

    if 'discord mod' == message.content.lower():
        await message.channel.send("Not gonna be active on Discord tonight. I'm meeting a girl (a real one) in half an hour (wouldn't expect a lot of you to understand anyway) so please don't DM me asking me where I am (im with the girl, ok) you'll most likely get aired because ill be with the girl (again I don't expect you to understand) shes actually really interested in me and its not a situation i can pass up for some meaningless Discord degenerates (because ill be meeting a girl, not that you really are going to understand) this is my life now. Meeting women and not wasting my precious time online, I have to move on from such simple things and branch out (you wouldnt understand)")

    if '!' in message.content:
        if message.content == '!ping':
            await message.channel.send('!pong')
        else:
            await message.channel.send('!')


bot.run(TOKEN)
