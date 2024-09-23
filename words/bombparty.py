from random import randint

taken = []
while True:
  sequence = input("\nWhat word to you want found? ")
  best = ""
  with open("words//allwords.txt", "r") as file:
    for line in file:
      word = line.strip()
      if sequence.upper() in word and (len(word) > len(best) or (len(word) == len(best) and randint(1,3) == 1)) and word not in taken:
          best = word
  if best == "":
    print("\nNo word found")
  else:
    print(best)
  taken.append(best)