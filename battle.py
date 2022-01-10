import discord
import json
from random import choice, sample
from utilities import getCardsWithStats, getCards, printCards, printTopCard

async def battle1v1(message, client):
    current_channel=message.channel
    opponent=message.mentions[0]
    if opponent==message.author:
        await current_channel.send("Please dont battle yourself!")
        return
    await current_channel.send(
        '{} has requested a battle with {}.\n Do you accept?(Press Y or yes to accept or anything else to deny.)'.format(
            message.author.mention, opponent.mention))
    def check(m):
        return m.author == opponent and m.channel == current_channel
    
    accept=['yes', 'y']
    message_confirm = await client.wait_for("message", check=check)
    if not str(message_confirm.content).lower().strip() in accept:
        await current_channel.send("Battle Denied!")
        return
    await current_channel.send("Battle Accepted!")
    await printCards(message_confirm)
    await printCards(message)

    p1=choice([message.author, message_confirm.author])
    p1_cards=getCardsWithStats(p1.id)
    p1_ShuffledCards=sample(p1_cards, len(p1_cards))

    p2=message_confirm.author if p1==message.author else message.author
    p2_cards=getCardsWithStats(p2.id)
    p2_ShuffledCards=sample(p2_cards, len(p2_cards))

    await current_channel.send("{} will start.".format(p1.mention))
    while True:
        await current_channel.send("{}, your current card is:".format(p1.mention))
        await printTopCard(current_channel,p1.id, p1_ShuffledCards)
        await current_channel.send("Choose an attribute by either entering the number on the left or attribute name.")
        def check_attribute(m):
            return m.channel == current_channel and m.author==p1
        notAttribute=True
        attributes=[
            "Overall Rating",
            "Value For Money",
            "Customer Rating"]        
        while notAttribute:
            attribute = await client.wait_for("message", check=check_attribute)
            if attribute.content.isdecimal():
                if int(attribute.content)<=len(attributes) and int(attribute.content)>0:
                    notAttribute=False
                    attribute.content=attributes[int(attribute.content)-1]
                else:
                    # with open('log.txt', 'w+') as outfile:
                    #     outfile.write(str(attribute.content))
                    await current_channel.send("Shwooop! This is a wrong number.")
            else:
                for i in attributes:
                    if attribute.content.lower().strip()==i.lower():
                        notAttribute=False
                        attribute.content=attribute.content.title()
                if notAttribute==True:
                    with open('log.txt', 'a+') as outfile:
                        outfile.write(str(attribute.content)+'\n')
                    await current_channel.send("Shwooop! This is a wrong attribute.")
        
        if p1_ShuffledCards[0][attribute.content] >= p2_ShuffledCards[0][attribute.content]:
            txt="{} won this round.\n{} had:".format(p1.mention, p2.mention)
            
            await current_channel.send(txt)
            await printTopCard(current_channel, p2.id, p2_ShuffledCards)
            
            p1_ShuffledCards.append(p1_ShuffledCards.pop(0))
            p1_ShuffledCards.append(p2_ShuffledCards.pop(0))

            if len(p2_ShuffledCards)==0:
                txt="{} has won! You have earned 20 flight tickets!".format(p1.mention)
                with open('user_data.json', 'r') as json_file:
                    data = json.load(json_file)
                    data[str(p1.id)]['Tickets']+=20
                    txt+="\nYou now have {} flight tickets!".format(data[str(p1.id)]['Tickets'])
                    with open('user_data.json', 'w') as output_file:
                        json.dump(data,output_file)
                await current_channel.send(txt)
                break
            else:
                await current_channel.send("{} has {} cards left!\n{} has {} cards left!".format(p1.mention, len(p1_ShuffledCards), p2.mention, len(p2_ShuffledCards)))
        else:
            await current_channel.send("{} won this round.".format(p2.mention))
            await current_channel.send("{} had:".format(p2.mention))
            await printTopCard(current_channel,p2.id, p2_ShuffledCards)
            p2_ShuffledCards.append(p2_ShuffledCards.pop(0))
            p2_ShuffledCards.append(p1_ShuffledCards.pop(0))

            if len(p1_ShuffledCards)==0:
                txt="{} has won! You have earned 20 flight tickets!".format(p2.mention)
                with open('user_data.json', 'r') as json_file:
                    data = json.load(json_file)
                    data[str(p2.id)]['Tickets']+=20
                    txt+="\nYou now have {} flight tickets!".format(data[str(p2.id)]['Tickets'])
                    with open('user_data.json', 'w') as output_file:
                        json.dump(data,output_file)
                await current_channel.send(txt)
                break
            else:
                await current_channel.send("{} has {} cards left!\n{} has {} cards left!".format(p1.mention, len(p1_ShuffledCards), p2.mention, len(p2_ShuffledCards)))
            p2, p1 = p1, p2
            p1_ShuffledCards, p2_ShuffledCards = p2_ShuffledCards, p1_ShuffledCards
            p1_cards, p2_cards=p2_cards, p1_cards
