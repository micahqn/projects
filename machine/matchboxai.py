from random import *
from sqlitedict import SqliteDict
import math
#https://www.askpython.com/python/examples/save-data-in-python

current_grid = [
    [" ", " ", " "], 
    [" ", "O", "X"], 
    [" ", " ", "X"]
    ]

class MatchboxModel:
    def __init__(self, name):
        self.name = name
        self.memory = {
            "#########" : {"11":1, "12":1, "13":1, "21":1, "22":1, "23":1, "31":1, "32":1, "33":1}
        }

def save(key, value, cache_file="cache.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value
            mydict.commit()
    except Exception as ex:
        print("Error during storing data (Possibly unsupported):", ex)

def load(key, cache_file="cache.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key]
        return value
    except Exception as ex:
        print("Error during loading data:", ex)

def printBoard(grid):
    emptyrow = "     |     |     \n"
    fullrow  = "-----|-----|-----"
    vrow = lambda row: f"  {row[0]}  |  {row[1]}  |  {row[2]}  \n"
    for i in range(3):
        if i != 2: print((emptyrow+vrow(grid[i])+emptyrow+fullrow))
        else: print((emptyrow+vrow(grid[i])+emptyrow))

def gridToString(grid):
    rows = []
    for row in grid:
        rows.append("".join(row))
    return "".join(rows).replace(" ", "#")

def stringToGrid(string):
    grid = [["", "", ""], ["", "", ""], ["", "", ""]]
    count = 0
    for char in string:
        grid[int(count/3-count/3%1)][count%3] = char if char != "#" else " "
        count += 1
    return grid

def findAllPossibleMoves(grid):
    moves = {}
    for row in range(3):
        for column in range(3):
            if grid[row][column] == " ": moves[str(row+1)+str(column+1)] = 1
    return moves

def findCongruentGames(grid):
    def rotate(grid):
        newgrid = [list(reversed(x)) for x in zip(*grid)]
        return newgrid
    
    congruent_grids = [grid]
    for _ in range(3):
        congruent_grids.append(rotate(congruent_grids[-1]))
        
    return congruent_grids

for game in findCongruentGames(current_grid):
    printBoard(game)

CurrentMatchBoxAi = MatchboxModel("Bartholomew")
previous_move = [] #gridstring, move

while True:
    print("Vs", CurrentMatchBoxAi.name)
    printBoard(current_grid)
    plr_input = input("enter coords (row, column) or reward/punish (r or p) previous move ")

    if len(plr_input) == 2:
        current_grid[int(plr_input[0])-1][int(plr_input[1])-1] = "X"

    elif plr_input == "r" and previous_move != []:

        CurrentMatchBoxAi.memory[previous_move[0]][previous_move[1]] += 15
        input("rewarded, enter to continue ")
        continue

    elif plr_input == "p" and previous_move != []:
        CurrentMatchBoxAi.memory[previous_move[0]][previous_move[1]] = max(0, CurrentMatchBoxAi.memory[previous_move[0]][previous_move[1]] - 10)

        input("punished, enter to continue ")
        print(CurrentMatchBoxAi.memory[previous_move[0]])
        continue

    else:
        current_grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        if randint(1,1) == 1: continue

    gridId = gridToString(current_grid)

    if not gridId in CurrentMatchBoxAi.memory:
        CurrentMatchBoxAi.memory[gridId] = findAllPossibleMoves(current_grid)

    pm = [possible for possible in CurrentMatchBoxAi.memory[gridId]] #possible moves
    pick = choice(choices([p for p in pm], [CurrentMatchBoxAi.memory[gridId][q] for q in pm], k=100))
    current_grid[int(pick[0])-1][int(pick[1])-1] = "O"
    previous_move = [gridId, pick]

