import discord
import json


async def cardstrade(message, client):
    await message.channel.send('{0} wants to trade'.format(message.author.mention))
    await message.channel.send("Anyone wanting to trade these cards, .accept is the command")
    accept=['.accept']
    def check(m):
        return m.channel == message.channel and message.author != m.author
    def checkChannel(m):
        return m.channel == message.channel
    msg = await client.wait_for("message", check=check)
    if str(msg.content).lower() in accept:
        await message.channel.send('{0} has accepted the trade'.format(msg.author.mention))
        await printCards(message)
        await message.channel.send('{0} which card do you wish to trade'.format(message.author.mention))
        cardOne=await client.wait_for("message",check=checkChannel)
        if (check_validity(cardOne)):
            await printCards(msg)
            await message.channel.send('{0} which card do you wish to trade'.format(msg.author.mention))
            cardTwo=await client.wait_for("message",check=checkChannel)
            if(check_validity(cardTwo)):
                await message.channel.send('{0} send .accept to accept the trade'.format(message.author.mention))
                

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


                    
def check_validity(message):
    usercards=getCards(message)
    return message.content in usercards
    