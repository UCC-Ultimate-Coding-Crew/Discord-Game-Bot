async def helpout(message):
    print("Welcome to the Airline Trump Cards")
    print("Here a list of commands to play around with:")
    await message.channel.send("Welcome to the Airline Trump Cards")
    await message.channel.send("Here a list of commands to play around with:")
    
    statements=[".start assigns you 2 random cards in the start",".battle gets you into the battleground to face an opponent"]
    printing="```"
    for i in statements:
        printing+="\n"
        printing+=i
        print('yolo', printing)

    printing="```"
    await message.channel.send(printing)
    print(printing)