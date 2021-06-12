import discord
import json
from random import choice, sample

async def getCards(message):
    await message.channel.send("{}\nYour Cards:".format(message.author.mention))
    with open('user_data.json') as json_file:
            data = json.load(json_file)
            if str(message.author.id) in data.keys():
                for i in data[str(message.author.id)]['Cards']:
                    j= data[str(message.author.id)]['Cards'][i]
                    with open('cards.json') as card:
                        airline = json.load(card)
                        usercards=airline[j]["Airline Name"]
                        await message.channel.send(usercards)

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
    await getCards(message_confirm)
    await getCards(message)
    current_player=choice([message.author, opponent])
    # p1_cards=sample(test_list, len(test_list))
    # p2_cards
    # while True:
        