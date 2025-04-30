from pathlib import Path
from random import choices, choice, shuffle
from inflection import tableize
import os
from google import genai

client = genai.Client(api_key="AIzaSyBoVIii97ga5mTa6C9r0JQCVMJvDRLI_wM") #pls don't steal my key i dont feel like hiding it 🙏
chat = client.chats.create(model="gemini-2.0-flash")

notes_dir = Path.cwd() / "machine" / "notes"
files = list(notes_dir.rglob("*.txt*"))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
desiredTopics = []
answer = input("would you like to study multiple topics? (y/n) ")
if answer == "y":
    while True:
        clear()
        for file in files:
            print(f"{files.index(file)+1}: {file.name.replace('.txt', '')}")
        answer2 = input("what would you like to study? enter 'STOP' to finish ")
        if answer2 != "STOP": 
            desiredTopics.append(files[int(answer2)-1])
            files.pop(int(answer2)-1)
        else:
            break
else:
    for file in files:
        print(f"{files.index(file)+1}: {file.name.replace('.txt', '')}")
    answer2 = int(input("what would you like to study? "))
    desiredTopics.append(files[answer2-1])

lines = []

for directory in desiredTopics:
    with open(directory, "r") as file:
        for line in file:
            note = line.strip()
            if " - " in note:
                lines.append(note)

weighted_questions = {}
for question in lines:
    weighted_questions[question] = 2


def questioning(questions):
    question_weights, possibles = [], []
    for q in questions:
        possibles.append(q)
        question_weights.append(questions[q])

    test = choices(possibles, weights=question_weights, k=1)[0]
    word, definition = test.split(" - ", 1)

    print(chat.send_message(message=[f"create a random scenario or question, where the answer is '{word}' and the definition is '{definition}.' Just include the question by itself, and don't say the answer. write it in an AP style format where the question reveals a high understanding of the answer"]).text)

    answer = input("Enter answer or type 'hint': ")
    if tableize(answer) == tableize(word):
        input("Good Job")
        questions[test] -= 1
        if questions[test] == 0:
            del questions[test]
            if questions == {}:
                input("You have mastered this set!")
                return
    elif answer == "hint":
        clear()
        print(chat.send_message(message=[f"restate the previous question and give a hint on the previous question, where the answer is '{word}' and the definition is '{definition}.'"]).text)
        answer = tableize(input("Enter answer: "))
        if answer == tableize(word):
            input("Good Job")
            questions[test] -= 1
            if questions[test] == 0:
                del questions[test]
                if questions == {}:
                    input("You have mastered this set!")
                    return
        else:
            print(f"Answer was {word}")
            input(chat.send_message(message=[f"on the previous question, explain why the answer is not '{answer}' and the real answer is '{word}.' Give a large breakdown why, or if their answer is more correct than the real answer, address it"]).text)


    else:
        print(f"Answer was {word}")
        input(chat.send_message(message=[f"on the previous question, explain why the answer is not '{answer}' and the real answer is '{word}.' Give a large breakdown why, or if their answer is more correct than the real answer, address it"]).text)
    clear()
    questioning(questions)

clear()
questioning(weighted_questions)

