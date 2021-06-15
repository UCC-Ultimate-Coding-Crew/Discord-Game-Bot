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
			else:
				return []

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

def getAirlineCode(input):
	with open('user_data.json') as json_file:
		data=json.load(json_file)
		return data[str(input.author.id)]['Cards'][input.content]



async def printCards(message):
	# await message.channel.send("{0} Your Cards:".format(message.author.mention))
	txt="{0} Your Cards:\n".format(message.author.mention)
	for i in getCards(message.author.id):
		txt+=str(i)+'\n'
	await message.channel.send(txt)


def getCardCodes(message):
	with open('user_data.json') as json_file:
		data = json.load(json_file)
		cards=data[str(message.author.id)]["Cards"]
		# ls=[]
		# for i in data[str(message.author.id)]["Cards"]:
		# 	ls.append(data[str(message.author.id)]["Cards"][i])
		# 	return ls
		return cards

async def printCardCodes(message):
	await message.channel.send("{0} Your Cards:".format(message.author.mention))
	cards=getCardCodes(message)
	pairs=cards.items()
	txt='```'
	for key,value in pairs:
		name=getAirlineName(value)
		txt+='{0} :\t {1}'.format(key,name)+'\n'
	txt+='```'
	await message.channel.send(txt)

def getAirlineName(value):
	with open('cards.json') as card:
		airline = json.load(card)
		return airline[value]["Airline Name"]


async def printTopCard(channel, uid, shuffled=None):
	if shuffled == None:
		shuffled=getCardsWithStats(uid)
	txt='```Airline Name\t'+shuffled[0]['Airline Name']+'\n'
	count=1
	for j in shuffled[0].items():
		if j[0]=='Rarity' or j[0]=='Airline Name':
			continue
		txt+=str(count)+'. '+str(j[0])+":\t"+str(j[1])+"\n"
		count+=1
	txt+='```'
	await channel.send(txt)

def getTotalCards(message):
	count=0
	with open('user_data.json') as json_file:
		data = json.load(json_file)
		for i in data[str(message.author.id)]['Cards']:
			count+=1
		return count

def completeTrade(cardOne,cardTwo):
	codeOne=getAirlineCode(cardOne) #The card the 2nd person will get
	codeTwo=getAirlineCode(cardTwo)
	datafile=open('user_data.json','r')
	file=json.load(datafile)
	file[str(cardOne.author.id)]['Cards'].pop(cardOne.content)
	toAdd={cardOne.content:codeTwo}
	file[str(cardOne.author.id)]['Cards'].update(toAdd)


	file[str(cardTwo.author.id)]['Cards'].pop(cardTwo.content)
	toAdd={cardTwo.content:codeOne}
	file[str(cardTwo.author.id)]['Cards'].update(toAdd)
	output=open('user_data.json', 'w')
	json.dump(file, output)
	