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

client= discord.Client()

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.start'):
        await create_new_user(message)
    if message.content.startswith('.battle'):
        await battle2v2(message)
    if message.content == '.help':
        await helpout(message)

token=open("token.txt", 'r').read()
client.run(token)