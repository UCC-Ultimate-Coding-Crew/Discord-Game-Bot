import discord
import json

async def battle2v2(message, client):
    opponent=message.mentions[0]
    print(message.mentions)
    await message.channel.send('{} has requested a battle with {}.\n Do you accept?[Y/n]'.format(message.author.mention, opponent.mention))
    
    def check(m):
        return m.author == opponent and m.channel == message.channel
    accept=['yes', 'y']
    msg = await client.wait_for("message", check=check)
    if str(msg.content).lower() in accept:
        await msg.channel.send("Accepted")
    else:
        await msg.channel.send("Battle Denied")
    