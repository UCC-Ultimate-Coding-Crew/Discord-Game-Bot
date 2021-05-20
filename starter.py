import discord
import json

data={
    'Flight1':{
        'Customer Satisfaction':0,
        'Overall Rating':0,
        'Value For Money':0
    }
}


client= discord.Client()

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        await message.channel.send('Hello World!')

    if message.content.startswith('.start'):
        with open('user_data.json') as json_file:
            data = json.load(json_file)
            print(data.keys(), type(message.author.id))
            if str(message.author.id) in data.keys():
                print('already exists')
                await message.channel.send('User already initialized')
            else:
                post_data={
                    message.author.id:'Initialized'
                }
                data.update(post_data)
                with open('user_data.json', 'w') as outfile:
                    json.dump(data, outfile)
                    await message.channel.send('initialized')


token=open(r"Discord-Game-Bot/token.txt", 'r').read()
client.run(token)