import discord
import json
from random import choice, sample
from utilities import getCardsWithStats, getCards, printCards, printTopCard
# async def getCards(message):
#     await message.channel.send("{}\nYour Cards:".format(message.author.mention))
#     with open('user_data.json') as json_file:
#             data = json.load(json_file)
#             if str(message.author.id) in data.keys():
#                 for i in data[str(message.author.id)]['Cards']:
#                     j= data[str(message.author.id)]['Cards'][i]
#                     with open('cards.json') as card:
#                         airline = json.load(card)
#                         usercards=airline[j]["Airline Name"]
#                         await message.channel.send(usercards)

async def battle2v2(message, client):
    opponent=message.mentions[0]
    await message.channel.send('{} has requested a battle with {}.\n Do you accept?[Y/n]'.format(message.author.mention, opponent.mention))
    def check(m):
        return m.author == opponent and m.channel == message.channel
    
    accept=['yes', 'y']
    message_confirm = await client.wait_for("message", check=check)
    if not str(message_confirm.content).lower() in accept:
        await message_confirm.channel.send("Battle Denied")
        return
    await message_confirm.channel.send("Accepted")
    await printCards(message_confirm)
    await printCards(message)

    p1=choice([message.author, opponent])
    p1_cards=getCardsWithStats(message.author.id)
    p1_ShuffledCards=sample(p1_cards, len(p1_cards))
    p2=opponent if p1==message.author else message.author
    p2_cards=getCardsWithStats(message_confirm.author.id)
    p2_ShuffledCards=sample(p2_cards, len(p2_cards))

    await message.channel.send("{} will start.".format(p1.mention))
    while True:
        await message.channel.send("{}, your current card is:".format(p1.mention))
        await printTopCard(message.channel,p1.id, p1_ShuffledCards)
        await message.channel.send("Choose an attribute.")
        def check_attribute(m):
            notAttribute=True
            attributes=[
                "Overall Rating",
                "Value For Money",
                "Customer Rating"]
            for i in p1_ShuffledCards:
                if m.content in attributes:
                    notAttribute=False
            return m.channel == message.channel and not notAttribute
        attribute = await client.wait_for("message", check=check_attribute)
        if p1_ShuffledCards[0][attribute.content] > p2_ShuffledCards[0][attribute.content]:
            await message.channel.send("{} won this round.".format(p1.mention))
            await message.channel.send("{} had:".format(p2.mention))
            await printTopCard(message.channel, p2.id, p2_ShuffledCards)
            
            p1_ShuffledCards.append(p1_ShuffledCards.pop(0))
            p1_ShuffledCards.append(p2_ShuffledCards.pop(0))

            if len(p2_ShuffledCards)==0:
                await message.channel.send("{} has won!".format(p1.mention))
                break
        else:
            await message.channel.send("{} won this round.".format(p2.mention))
            await message.channel.send("{} had:".format(p1.mention))
            await printTopCard(message.channel,p1.id, p1_ShuffledCards)
            p2_ShuffledCards.append(p2_ShuffledCards.pop(0))
            p2_ShuffledCards.append(p1_ShuffledCards.pop(0))

            if len(p1_ShuffledCards)==0:
                await message.channel.send("{} has won!".format(p2.mention))
                break
            p2, p1 = p1, p2
            p1_ShuffledCards, p2_ShuffledCards = p2_ShuffledCards, p1_ShuffledCards
            p1_cards, p2_cards=p2_cards, p1_cards
