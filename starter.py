import discord
import json
from random import random, choice
from create_user import create_new_user
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

token=open(r"Discord-Game-Bot/token.txt", 'r').read()
client.run(token)