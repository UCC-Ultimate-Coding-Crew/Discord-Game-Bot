import discord
import json
from random import random, choice
from create_user import create_new_user
from battle import battle2v2
from help import helpout
from discord.ext import commands
from discord.ext.commands import Bot

data={
    'Flight1':{
        'Customer Satisfaction':0,
        'Overall Rating':0,
        'Value For Money':0
    }
}

BOT_PREFIX = (".")
bot = commands.Bot(command_prefix=BOT_PREFIX)
client= discord.Client()

@bot.event
async def on_ready():
    print("Ready")

@bot.command(pass_context=True)
async def battle(ctx):
    channel = ctx.message.channel
    # t1 = time.perf_counter()
    await bot.send_typing(channel)
    # t2 = time.perf_counter()
    await bot.say('{} has requested a battle'.format(ctx.author))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.start'):
        await create_new_user(message)
    # if message.content.startswith('.battle'):
    #     await battle2v2(message)
    if message.content == '.help':
        await helpout(message)

token=open("Discord-Game-Bot/token.txt", 'r').read()
client.run(token)