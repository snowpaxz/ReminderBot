""" A simple Discord bot made to reply to exclamation points.
    TODO: Add time based reminders to different events, like due dates """
import os

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))

intents = discord.Intents.all()

bot = commands.Bot(command_prefix= '.', intents=intents)

@bot.event
async def on_ready():
    """Waits for bot to initialize, then prints bot & guild info"""
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))
    print('Bot is ready to be used')

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

    if '!' in message.content:
        if message.content == '!ping':
            await message.channel.send('!pong')
        else:
            await message.channel.send('!')

bot.run(TOKEN)
