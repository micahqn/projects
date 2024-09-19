thought_process = False

map = int(input("\nWhat square map do you want solved? (i.e 4 or 5)"))
letters = input("\nInput all letters in map, type order like reading a book ")

if len(letters) != map*map:
  print(f"\nInvalid input, {len(letters)} letters given, {map*map} letters needed")
  exit()
if not letters.isalpha():
  print("\nInvalid input, given letters include special characters")
  exit()

letters = letters.upper()

grid = []

#word functions
def find_possible(begin):
  possible = []
  with open("allwords.txt", "r") as file:
    for line in file:
      word = line.strip()
      if word.startswith(begin):
        possible.append(word)
  return possible

def sanitycheck(possible, begin):
  return any(word.startswith(begin) for word in possible)

def aWord(given):
  with open("allwords.txt", "r") as file:
    for line in file:
      word = line.strip()
      if word == given:
        return True
  return False


#classes
class Square:
  global grid
  def __init__(self, letter, x, y):
    self.letter = letter
    self.x = x
    self.y = y
    self.neighbors = []
  def find_neighbors(self):
    directions = [[-1, -1], [0,-1], [1, -1], [-1, 0], [1, 0],[-1, 1], [0, 1], [1, 1]]
    for direction in directions:
      x = self.x + direction[0]
      y = self.y + direction[1]
      if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
        self.neighbors.append(grid[x][y])

class Path:
  global grid
  def __init__(self, order):
    self.order = order
    word = []
    for square in self.order:
      word.append(square.letter)
    self.word = "".join(word).upper()
    self.possible = find_possible(self.word)

  def construct_word(self):
    word = []
    for square in self.order:
      word.append(square.letter)
    return "".join(word).upper()
    

#function for finding all possible paths for squares
def findconnectionsofsquare(startsquare):
  alive_paths = [Path([startsquare])]
  dead_paths = []
  
  while alive_paths != []:
    for path in alive_paths:
      branchingpath = path.order[-1]
      nextletters = branchingpath.neighbors

      for square in nextletters:
        if square in path.order:
          if thought_process: print("collided with path")
          continue
        if not sanitycheck(path.possible, path.word+square.letter):
          if thought_process: print("dead end", path.word+square.letter)
          continue
          
        if thought_process: print("success", path.word+square.letter)
        alive_paths.append(Path(path.order+[square]))
      dead_paths.append(path)
      alive_paths.remove(path)

  dead_paths = list(dict.fromkeys(dead_paths))
  all_paths = []
  for path in dead_paths:
    if not aWord(path.word):
      continue
    all_paths.append(path.word)
  all_paths = list(dict.fromkeys(all_paths))
  
  all_paths.sort(key=len, reverse=True)
  return all_paths

#grid generation
print()
for x in range(map):
  row = []
  for y in range(map):
    row.append(Square(letters[x*map+y], x, y))
  grid.append(row)
  print("   ".join(square.letter for square in row)+"\n")

for row in grid:
  for square in row:
    square.find_neighbors()

all_answers = []

for row in grid:
  for square in row:
    print("Square", (row.index(square)+1)+grid.index(row)*len(grid), ("("+str(square.letter)+")"), "is connected to...")
    connections = findconnectionsofsquare(square)
    if connections == []:
      print("No connections")
      continue
    for path in connections:
      print(path)
    all_answers += connections
    print()

all_answers = list(dict.fromkeys(all_answers))
all_answers.sort(key=len, reverse=True)
print("All possible words:")
print(" ".join(all_answers))
