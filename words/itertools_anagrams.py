import itertools
from time import time

orgin = input("\nEnter letters to unscramble: ")
permutations = []
anagrams = []
start = time()

for i in range(len(orgin), 0, -1):
    for permutation in itertools.permutations(orgin, i):
        word = "".join(sorted(list(permutation))).lower()
        permutations.append(word)


permutations.sort(key=len, reverse=True)
permutations = list(dict.fromkeys(permutations))


with open("words//allwords.txt", "r") as file:
  for line in file:
    word = line.strip()
    if "".join(sorted(word.lower())) in permutations and word not in anagrams:
      anagrams.append(word)


anagrams.sort(key=len, reverse=True)
print(" ".join(anagrams))
print(f"\n{len(anagrams)} words in total")
print(f"elapsed time: {round(time()-start, 3)}s")