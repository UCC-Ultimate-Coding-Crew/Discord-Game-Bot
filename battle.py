import discord
import json

async def battle2v2(message):
    opponent=message.mentions[0]
    # opponent = discord.User(opponent)
    print(message.mentions)
    await message.channel.send('{} has requested a battle with {}.\n Do you accept?[Y/n]'.format(message.author.mention, opponent.mention))