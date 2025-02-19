from google import genai
import os

client = genai.Client(api_key="AIzaSyBoVIii97ga5mTa6C9r0JQCVMJvDRLI_wM")
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


while True:
    choice = input("would you like to load the previous file? (y/n)")
    match choice:
        case "y":
            break

        case "n":
            erase()

            os.system('cls' if os.name == 'nt' else 'clear')
            response = chat.send_message(message=["You are a game master, and you are making the player play a fantasy rpg, to go on a large adventure to kill a dragon across the continent. They begin in a small town in the country side, and they must defeat monsters. Begin by asking for the person's name, and remember it"])
            print(response.text)
            save(response.text)
            break

        case _:
            pass



while True:
    
    answer = input("\n")
    save(answer, "player")

    response = chat.send_message(message=[answer, "You are a game master, create scenarios and choices for the player, they are in medieval europe with kings and queens, with magic, swordsmanship and monsters, make the prompts descriptive but not too long."])
    save("\n"+response.text)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(response.text)
    
