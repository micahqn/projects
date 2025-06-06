import itertools
from time import time

orgin = input("\nEnter letters to unscramble: ")
combinations = []
anagrams = []
start = time()

for i in range(len(orgin), 0, -1):
    for combination in itertools.combinations(orgin, i):
        word = "".join(sorted(list(combination))).lower()
        combinations.append(word)


combinations.sort(key=len, reverse=True)
combinations = list(dict.fromkeys(combinations))


with open("words//allwords.txt", "r") as file:
  for line in file:
    word = line.strip()
    if "".join(sorted(word.lower())) in combinations and word not in anagrams:
      anagrams.append(word)


anagrams.sort(key=len, reverse=True)
print(" ".join(anagrams))
print(f"\n{len(anagrams)} words in total")
print(f"elapsed time: {round(time()-start, 3)}s")