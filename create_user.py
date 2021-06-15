import discord
import json
import datetime
from random import random, choice

def get_possible_cards():
    rand_val=random()
    chosen_type=''
    if rand_val>0.8:
        chosen_type='Gold'
    elif rand_val>0.5:
        chosen_type='Silver'
    else:
        chosen_type='Bronze'

    possible_cards=[]

    with open('cards.json') as card_data:
        cards=json.load(card_data)
        for i in cards:
            if cards[i]['Rarity']==chosen_type:
                possible_cards.append(i)
    return possible_cards

async def create_new_user(message):
    with open('user_data.json') as json_file:
            data = json.load(json_file)
            if str(message.author.id) in data.keys():
                print('already exists')
                await message.channel.send('You already have an account!')

            else:
                chosen_cards=[choice(get_possible_cards()) for i in range(2)]
                
                post_data={
                    message.author.id:{
                        'deckSize':0,
                        'Cards':{},
                        'Tickets':10,
                        'LastClaimed': datetime.date.today().strftime("%d %m %Y")
                    }
                }
                for i in range(len(chosen_cards)):
                    post_data[message.author.id]['deckSize']+=1
                    post_data[message.author.id]['Cards'][str(i)]=chosen_cards[i]
                data.update(post_data)
                with open('user_data.json', 'w') as outfile:
                    json.dump(data, outfile)
                    await message.channel.send('User has now been initialized')
                    await message.channel.send('You get 10 coins for creating an account!')
                    with open('cards.json') as card_data:
                        cards=json.load(card_data)
                        for i in range(post_data[message.author.id]['deckSize']):
                            card=cards[post_data[message.author.id]['Cards'][str(i)]]['Airline Name']
                            await message.channel.send('You have been given: {0}!'.format(card))