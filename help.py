async def helpout(message):
    await message.channel.send("Welcome to the Airline Trump Cards")
    await message.channel.send("Here a list of commands to play around with:")
    
    statements=[
        "    .help gets you the help menu!",
        "    .start assigns you 2 random cards in the start",
        "    .battle gets you into the battleground to face an opponent",
        "    .trade allows you to swap cards with any interested player",
        "    .claim gets you 5 flight tickets daily",
        "    .tickets shows your current flight tickets",
        "    .market brings you to the marketplace"
        ]
    printing="```"
    for i in statements:
        printing+="\n"
        printing+=i
    printing+="```"
    await message.channel.send(printing)
