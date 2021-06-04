import discord
import json

async def battle2v2(message):
    x=message.content
    print(x)
    await message.channel.send('```You have requested a battle```')