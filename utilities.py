import discord 
import json

def getCards(uid):
	with open('user_data.json') as json_file:
			data = json.load(json_file)
			if str(uid) in data.keys():
				ls=[]
				for i in data[str(uid)]['Cards']:
					j= data[str(uid)]['Cards'][i]
					with open('cards.json') as card:
						airline = json.load(card)
						usercards=airline[j]["Airline Name"]
						ls.append(usercards)
				return ls

def getCardsWithStats(uid):
	with open('user_data.json') as json_file:
			data = json.load(json_file)
			if str(uid) in data.keys():
				ls=[]
				for i in data[str(uid)]['Cards']:
					j= data[str(uid)]['Cards'][i]
					with open('cards.json') as card:
						airline = json.load(card)
						usercard=airline[j]
						ls.append(usercard)
				return ls

async def printCards(message):
	await message.channel.send("{0} Your Cards:".format(message.author.mention))
	for i in getCards(message.author.id):
		await message.channel.send(i)

async def printTopCard(channel, uid, shuffled=None):
	if shuffled == None:
		shuffled=getCardsWithStats(uid)
	txt='```'
	for j in shuffled[0].items():
		txt+=str(j[0])+":\t"+str(j[1])+"\n"
	txt+='```'
	await channel.send(txt)