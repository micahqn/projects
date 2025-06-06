
game = input("1 : anagrams\n2 : bomb party\n3 : word hunt\ntype game you want to play: ")

file_name = ""

if game == "1":
  file_name = "words//anagrams.py"
elif game == "2":
  file_name = "words//bombparty.py"
elif game == "3":
  file_name = "words//wordhunt.py"

if file_name == "":
  print("\ninvalid input")
  exit()
with open(file_name) as f:
  exec(f.read())
