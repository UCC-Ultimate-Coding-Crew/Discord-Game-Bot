
async def helpout():
    print("Welcome to the Airline Trump Cards")
    print("Here a list of commands to play around with:")

    statements=["   .help gets you the help menu!","   .start assigns you 2 random cards in the start","   .battle gets you into the battleground to face an opponent"]

    printing="```"
    for i in statements:
        printing+="\n"
        printing+=i
        

    printing="```"
    print(printing)