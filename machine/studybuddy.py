from pathlib import Path
from random import choices, choice, shuffle
from inflection import tableize
import os

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
    print(definition)
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
        print(definition+"\n")
        mcq = []
        mcq.append(word)
        for i in range(3):
            mcq.append(choice(list(questions)).split(" - ", 1)[0])
        shuffle(mcq)
        for mca in mcq:
            print(mca)
        answer = tableize(input("Enter answer or type 'hint': "))
        if answer == tableize(word):
            input("Good Job")
            questions[test] -= 1
            if questions[test] == 0:
                del questions[test]
                if questions == {}:
                    input("You have mastered this set!")
                    return
        else:
            input(f"Answer was {word}")


    else:
        input(f"Answer was {word}")
    clear()
    questioning(questions)

clear()
questioning(weighted_questions)

