import discord
from utilities import getTotalCards, printCardCodes, completeTrade
import json

async def cardstrade(message, client):
	await message.channel.send('{0} wants to trade'.format(message.author.mention))
	await message.channel.send("Anyone wanting to trade these cards, .accept is the command")
	accept=['.accept']

	def check(m):
		return m.channel == message.channel and message.author != m.author
	def checkOne(m):
		return m.channel == message.channel and message.author == m.author
	def checkTwo(m):
		return m.channel == message.channel and msg.author == m.author
	msg = await client.wait_for("message",check=check) 
	if str(msg.content).lower() in accept:
		await message.channel.send('{0} has accepted the trade'.format(msg.author.mention))
		await printCardCodes(message)
		await message.channel.send('{0} enter the card number on the left of the card you wish to trade'.format(message.author.mention))
		while True:
			cardOne = await client.wait_for(("message"), check=checkOne) 
			if (check_validity(cardOne)):
				break
			else:
				await message.channel.send('Please enter a valid card number')
		await printCardCodes(msg)
		await message.channel.send('{0} enter the card number on the left of the card you wish to trade'.format(msg.author.mention))
		while True:
			cardTwo = await client.wait_for(("message"), check=checkTwo) 
			if (check_validity(cardTwo)):
				break
			else:
				await message.channel.send('Please enter a valid card number')
		await message.channel.send('{0} send .accept to accept the trade'.format(message.author.mention))
		input = await client.wait_for("message",check=checkOne)
		if str(input.content).lower() in accept:
			completeTrade(cardOne,cardTwo)
			await message.channel.send("Trade completed!")
			await printCardCodes(message)
			await printCardCodes(msg)


def check_validity(message):
	count= getTotalCards(message)
	input=int(message.content)
	if(input<count):
		return True