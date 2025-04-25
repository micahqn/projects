from google import genai
import os

client = genai.Client(api_key="AIzaSyBoVIii97ga5mTa6C9r0JQCVMJvDRLI_wM") #pls don't steal my key i dont feel like hiding it 🙏
chat = client.chats.create(model="gemini-2.0-flash")

def save(message, who="gamemaster"):
    with open("machine//zork_context.txt", "a") as file:
        if who == "player":
            message = " player answered with: "+message
        else:
            message = " you answered with: "+message
        file.write(message)

def erase():
    with open("machine//zork_context.txt", "w") as file:
        file.write("")

worlds = {
    "medieval" : ["You are generating me a game, and you are making the player play a medieval survival game, with monsters and magic. This world will have nobles, kings, queens, and knights. Begin by asking for the person's name, and remember it", "You are generating a game, create detailed scenarios and multiple choice questions for the player, This world will have nobles, kings, queens, and knights, this is a survival game and will last forever. Make sure to make plot and link them together in a sensible way. Also give short questions with descriptive words to describe the current setting. Do not make the player roll a die, you decide the outcome based off previous situations."],
    "future" : ["You are generating me a game, and you are making the player play a game based 200 years into the future. This game is in a lower-class district with a population mixed with robots, humans, and high crime. Begin by asking for the person's name, and remember it", "You are generating a game, create detailed scenarios and multiple choice questions for the player, This game is in a lower-class district with robots, criminals, and bounty hunters this is a survival game and will last forever. Make sure to make plot and link them together in a sensible way. Also give short questions with descriptive words to describe the current setting. Do not make the player roll a die, you decide the outcome based off previous situations."],
    "ronin" : ["You are generating me a game, and you are making the player play a game 500 years ago in feudal japan. The player will begin as a traveling ronin. Begin by asking for the person's name, and remember it", "You are generating a game, create detailed scenarios and multiple choice questions for the player, The player will begin as a traveling ronin in ancient feudal japan. Make sure to make plot and link them together in a sensible way. Also give short questions with descriptive words to describe the current setting. Do not make the player roll a die, you decide the outcome based off previous situations."],
    "steampunk" : ["You are generating me a game, and you are making the player play a steampunk roleplay game, with monsters and airships. This world was flooded, and bustling cities live on floating islands. Pirates roam the skies and rob cargo airships. Begin by asking for the person's name, and remember it", "You are generating a game, create detailed scenarios and multiple choice questions for the player, This is a steampunk game, with monsters and airships. This world was flooded, and bustling cities live on floating islands. Pirates roam the skies and rob cargo airships., this is a survival game and will last forever. Make sure to make plot and link them together in a sensible way. Also give short questions with descriptive words to describe the current setting. Do not make the player roll a die, you decide the outcome based off previous situations."]
}


while True:
    choice = input("would you like to load the previous file? (y/n)")
    match choice:
        case "y":
            with open("machine//zork_context.txt", "r") as file:
                
                x = chat.send_message(message=[file.read(), "use this information to continue the game"])
                world = [0, "Create detailed scenarios and multiple choice questions for the player, islands. Continue the game with the given information, this is a survival game and will last forever. Make sure to make plot and link them together in a sensible way. Also give short questions with descriptive words to describe the current setting. Do not make the player roll a die, you decide the outcome based off previous situations"]
                print(x.text)
                break

        case "n":
            erase()
            os.system('cls' if os.name == 'nt' else 'clear')
            for key in worlds:
                print(key.title())
            world = worlds[input("Select a world ").lower()]
            

            os.system('cls' if os.name == 'nt' else 'clear')
            response = chat.send_message(message=[world[0]])
            print(response.text)
            save(response.text)
            break

        case _:
            pass



while True:
    
    answer = input("\n")
    save(answer, "player")

    response = chat.send_message(message=[answer, world[1]])
    save("\n"+response.text)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(response.text)
    
