from random import choice
from create_user import get_possible_cards
from utilities import getTotalCards, getAirlineName
import json

async def marketplace(message,client):
	def checkOne(m):
		return m.channel == message.channel and message.author == m.author
	await message.channel.send("Welcome to Marketplace")

	await message.channel.send(".newcards is the command to buy new cards (100 coins per card)")
	msg=await client.wait_for("message",check=checkOne) 
	if(str(msg.content)==".newcards"):
		await getnewcards(message)

async def getnewcards(message):
	with open('user_data.json') as json_file:
		data=json.load(json_file)
		money=data[str(message.author.id)]['Tickets']
		if(money>=100):
			data[str(message.author.id)]['Tickets']-=100
			choices=get_possible_cards()
			card=choice(choices)
			toAdd={getTotalCards(message):card}
			data[str(message.author.id)]['Cards'].update(toAdd)
			output=open('user_data.json','w')
			json.dump(data,output)
			airlineName=getAirlineName(card)
			await message.channel.send("{0} received: {1}".format(message.author.mention,airlineName))
			await message.channel.send("{0} has {1} coins remaining".format(message.author.mention,data[str(message.author.id)]['Tickets']))
		else:
			await message.channel.send("Not enough money :(")







