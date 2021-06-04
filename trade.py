import discord
import json

async def cardstrade(message):
    print(message.author.name)
    await message.channel.send('{0} wants to trade'.format(message.author))

    with open('user_data.json') as json_file:
            data = json.load(json_file)
            if str(message.author.id) in data.keys():
                for i in data[str(message.author.id)]['Cards']:
                    for j in data[str(message.author.id)]['Cards'][i]:
                        await message.channel.send(j)
                    
