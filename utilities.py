import discord 
import json

def getCards(message):
    with open('user_data.json') as json_file:
            data = json.load(json_file)
            if str(message.author.id) in data.keys():
                ls=[]
                for i in data[str(message.author.id)]['Cards']:
                    j= data[str(message.author.id)]['Cards'][i]
                    with open('cards.json') as card:
                        airline = json.load(card)
                        usercards=airline[j]["Airline Name"]
                        ls.append(usercards)
                return ls

async def printCards(message):
    await message.channel.send("{0} Your Cards:".format(message.author.mention))
    for i in getCards(message):
        await message.channel.send(i)