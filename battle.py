import discord
import json

async def battle2v2(message):
    x=message.content
    print(message.author.name)
    await message.channel.send('{0} has requested a battle'.format(message.author))