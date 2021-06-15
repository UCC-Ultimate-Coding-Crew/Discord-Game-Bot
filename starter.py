from market import marketplace
import discord
import json
import datetime
from random import random, choice
from create_user import create_new_user
from battle import battle1v1
from help import helpout
from trade import cardstrade
import os

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
        await battle1v1(message, client)
    if message.content == '.help':
        await helpout(message)
    if message.content == '.trade':
        await cardstrade(message, client)
    if message.content == '.market':
        await marketplace(message,client)
    if message.content == '.claim':
        today=datetime.date.today().strftime("%d %m %Y")
        with open('user_data.json') as json_file:
            data = json.load(json_file)
            date=data[str(message.author.id)]['LastClaimed']
            if(today>date):
                data[str(message.author.id)]['LastClaimed']=today
                data[str(message.author.id)]['Tickets']+=5
                with open('user_data.json', 'w') as output_file:
                    json.dump(data,output_file)
                await message.channel.send("You have claimed 5 Daily Flight Tickets. Check in tomorrow for more!")
            else:
                await message.channel.send("Already Claimed Today!")
    if message.content=='.tickets':
        with open('user_data.json') as json_file:
            data = json.load(json_file)
            await message.channel.send("You have {} flight tickets.".format(str(data[str(message.author.id)]['Tickets'])))

# token= os.environ.get("BOT_TOKEN")
token=open("token.txt", 'r').read()
client.run(token)