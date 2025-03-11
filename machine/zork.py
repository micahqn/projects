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
            with open("machine//zork_context.txt", "r") as file:
                if file.read() == "": continue
                print(file.read())
                _ = chat.send_message(message=[file.read()])
                input()
                break

        case "n":
            erase()

            os.system('cls' if os.name == 'nt' else 'clear')
            response = chat.send_message(message=["You are a game master, and you are making the player play a medieval survival game, with monsters and magic. This world will have nobles, kings, queens, and knights. Begin by asking for the person's name, and remember it"])
            print(response.text)
            save(response.text)
            break

        case _:
            pass



while True:
    
    answer = input("\n")
    save(answer, "player")

    response = chat.send_message(message=[answer, "You are a game master, create detailed scenarios and multiple choice questions for the player, This world will have nobles, kings, queens, and knights, this is a survival game and will last forever. Make sure to make plot and link them together in a sensible way. Also give short questions with descriptive words to describe the current setting. Do not make the player roll a die, you decide the outcome based off previous situations."])
    save("\n"+response.text)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(response.text)
    
