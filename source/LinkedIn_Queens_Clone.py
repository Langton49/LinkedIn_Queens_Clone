import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
from collections import deque

# Method to create a random area distribution for colonies on the grid and returning them in an array
# Function runs once, don't believe further optimization necessary
def assignAreaWeights(z):
    y = 64 - (z * 2)
    weights = [2] * z

    for i in range(z-1):
        x = randint(1, y - (z-i-1))
        weights[i] += x
        y -= x
    weights[z-1] += y
    weights = sorted(weights)
    return weights

# Method to check if a colony has more than one queen 
def checkColony(r, c):
    for i in queensColonies.keys():
        if (r, c) in queensColonies[i]:
            for t in queensColonies[i]:
                if t != (r, c) and placedQueen[t[0]][t[1]]:
                    messagebox.showinfo("Alert", "There is already a queen in this colony!")
                    break
            break

# Check whether first win condition (every colony has only one queen) has been satisfied
def firstWinCondition():
    queens = 0
    totalQueens = len(queensColonies)
    for i in queensColonies.values():
        for t in i:
            if placedQueen[t[0]][t[1]]:
                queens += 1
    return queens == totalQueens

# Check whether second win condition (no crowns are sharing a column or row) has beem satisfied
def secondWinCondition():
    rowsSet = set()
    colsSet = set()
    if firstWinCondition():
        for i in queensColonies.values():
            for t in i:
                if placedQueen[t[0]][t[1]]:
                    rowsSet.add(t[0])
                    colsSet.add(t[1])
        
        return len(rowsSet) == len(colsSet)
    return False

# Check whether third win condition (no queens are touching diagonally) has been satisfied 
def thirdWinCondition():
    if secondWinCondition():
        for i in queensColonies.values():
            for t in i:
                if placedQueen[t[0]][t[1]]:
                    if t[0]<7 and t[1]<7 and placedQueen[t[0]+1][t[1]+1]:
                        return False
                    if t[0]<7 and t[1]>0 and placedQueen[t[0]+1][t[1]-1]:
                        return False
                    if t[0]>0 and t[1]<7 and placedQueen[t[0]-1][t[1]+1]:
                        return False
                    if t[0]>0 and t[1]>0 and placedQueen[t[0]-1][t[1]-1]:
                        return False
        return True
    return False


xGrid = [[0 for _ in range(8)] for _ in range(8)] 

# Method to display that a colony can no longer have any more queens
def eliminateColony(r, c):
    for i in range(8):
        if i != c and placedQueen[r][i]:
             messagebox.showinfo("Alert", "Queen cannot go there")
             return
        elif i != c:
            if grid[r][i]['text'] != "x":
                grid[r][i].config(text="x")
            xGrid[r][i] += 1

    for i in range(8):
        if i != r and placedQueen[i][c]:
            messagebox.showinfo("Alert", "Queen cannot go there")
            return
        elif i != r:
            if grid[i][c]['text'] != "x":
                grid[i][c].config(text="x")
            xGrid[i][c] += 1
                
    if (r>0 and c<7 and placedQueen[r-1][c+1]) or (r<7 and c<7 and placedQueen[r+1][c+1]) or (r>0 and c>0 and placedQueen[r-1][c-1]) or (r<7 and c>0 and placedQueen[r+1][c-1]):
            messagebox.showinfo("Alert", "Queen cannot go there")
            return
    else:
        if r>0 and c<7:
            if grid[r-1][c+1]['text'] != "x":
                grid[r-1][c+1].config(text="x")
            xGrid[r-1][c+1] += 1

        if r<7 and c<7:
            if grid[r+1][c+1]['text'] != "x":
                grid[r+1][c+1].config(text="x")
            xGrid[r+1][c+1] += 1

        if r>0 and c>0:
            if grid[r-1][c-1]['text'] != "x":
                grid[r-1][c-1].config(text="x")
            xGrid[r-1][c-1] += 1
            
        if r<7 and c>0:
            if grid[r+1][c-1]['text'] != "x":
                grid[r+1][c-1].config(text="x")
            xGrid[r+1][c-1] += 1

    for i in queensColonies.keys():
        if (r, c) in queensColonies[i]:
            for t in queensColonies[i]:
                if t != (r, c) and not placedQueen[t[0]][t[1]]:
                    if grid[t[0]][t[1]]['text'] != "x":
                        grid[t[0]][t[1]].config(text="x") 
                    xGrid[t[0]][t[1]] += 1  
            break

# Method to display that a colony can have a queen placed in it when one is cleared
def clearColony(r, c):
    colony = set()
    for i in queensColonies.keys():
        if (r, c) in queensColonies[i]:
            colony = queensColonies[i]
            for t in queensColonies[i]:
                    if t != (r, c):
                        xGrid[t[0]][t[1]] -= 1
                        if not xGrid[t[0]][t[1]]:
                            grid[t[0]][t[1]].config(text="")
            break
    for i in range(8):
        if xGrid[r][i]:
            xGrid[r][i] -= 1
        if xGrid[i][c]:
            xGrid[i][c] -= 1
        if not xGrid[r][i]:
            grid[r][i].config(text="")
        if not xGrid[i][c]:
            grid[i][c].config(text="")

    if r>0 and c<7:
        xGrid[r-1][c+1] -= 1
        if not xGrid[r-1][c+1]:
            grid[r-1][c+1].config(text="")
    if r<7 and c<7:
        xGrid[r+1][c+1] -= 1
        if not xGrid[r+1][c+1]:
            grid[r+1][c+1].config(text="")
    if r>0 and c>0:
        xGrid[r-1][c-1] -= 1
        if not xGrid[r-1][c-1]:
            grid[r-1][c-1].config(text="")
    if r<7 and c>0:
        xGrid[r+1][c-1] -= 1
        if not xGrid[r+1][c-1]:
            grid[r+1][c-1].config(text="")

placedQueen = [[False for _ in range(8)] for _ in range(8)]

# Method to handle all button events
def drawX(button, r, c):
    if button['text'] == "x" and not placedQueen[r][c]:
        button.config(image=icon)
        placedQueen[r][c] = True
        eliminateColony(r, c)
        checkColony(r, c)
        if thirdWinCondition():
            messagebox.showinfo("Congratulations", "You have won!")
            return
    elif placedQueen[r][c]:
        button.config(image='', text='')
        placedQueen[r][c] = False
        clearColony(r, c)
    else:
        button.config(text="x")
        xGrid[r][c] += 1
    

# Initialize a 2D boolean array to show where queens have been placed in the grid and to show available space for helper
# algorithm to grow colony
valid = [[False for _ in range(8)] for _ in range(8)]

# List of possible colony colors
islandColors = ['red', 'green', 'aliceblue', 'yellow', 'cyan', 'deeppink', 'violet', 'orange', 'seagreen1']

# Method to map colonies randomly according to their assigned area
def helper(start, grid, weight, color):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    row, col = start
    valid[row][col] = True
    grid[row][col].config(bg=color)
    while weight[0]:
        if not directions:
            return
        move = choice(directions)
        ogRow, ogCol = row, col
        row += move[0]
        col += move[1]
        if 0 <= row <= 7 and 0 <= col <= 7 and not valid[row][col]:
            weight[0] -= 1
            helper((row, col), grid, weight, color)
        else:
            directions.remove(move)
            row = ogRow
            col = ogCol
            continue
    return

# Method to add uncolonized blocks to the nearest found colony 
def helper2(start):
    shuffle(directions)
    row = start[0]
    col = start[1]
    visited.add(start)
    for i in directions:
        nRow = row + i[0]
        nCol = col + i[1]
        if 0<=nRow<8 and 0<=nCol<8:
            if valid[nRow][nCol]:
                return (nRow, nCol)
            if (nRow, nCol) not in visited:
                discoveredColoniesQueue.append((nRow, nCol))
    return helper2(discoveredColoniesQueue.popleft())

# Method to get all blocks that belong to a queen's colony
def getColony(queen): 
    colonyColor = grid[queen[0]][queen[1]].cget("bg")
    for i in range(8):
        for j in range(8):
            if grid[i][j].cget("bg") == colonyColor:
                queensColonies[queen].add((i, j))

def revealQueen():
    shuffle(queensAvailable)
    randomQueen = queensAvailable[-1]
    drawX(grid[randomQueen[0]][randomQueen[1]], randomQueen[0], randomQueen[1])
    drawX(grid[randomQueen[0]][randomQueen[1]], randomQueen[0], randomQueen[1])
    queensAvailable.pop()
    


app = tk.Tk()
icon = tk.PhotoImage(file="../Assets/crown.png")
app.title("Queens")
app.geometry("700x700")
frame = tk.Frame(app)
frame.place(rely=0.5, relx=0.5, anchor="center")


# Create grid of buttons
grid = []
for i in range(8):
    rows = []
    for j in range(8):
        newButton = tk.Button(frame, width=5, height=2, bd=1, relief="solid")
        newButton.grid(row=i, column=j, sticky="nsew")
        rows.append(newButton)
    grid.append(rows)


# Initialize a grid to represent the open blocks available to queens
placementGrid = [[0 for _ in range(8)] for _ in range(8)]  

# Initialize a set for available rows and columns to place queens
availableRows = {0, 1, 2, 3, 4, 5, 6, 7}
availableCols = {0, 1, 2, 3, 4, 5, 6, 7}

# Initialize queens to keep track of the number of queens on the grid
queens = 0

# Initialize weightToButtonMap to assign colony weights to different queens
weightToButtonMap = {}

# Initialize queensColonies to hold all blocks that are a part of a queens colony
queensColonies = {}

while availableCols:
    # Convert currently available columns and rows into a list
    rList = list(availableRows)
    cList = list(availableCols)

    # Get a random row and a random column in the grid 
    row = choice(rList)
    col = choice(cList)

    # If the only remaining row-column combination does not fit into the grid, break out of the loop
    if len(rList) == 1:
        if placementGrid[row][col]:
            weightToButtonMap.clear()
            queensColonies.clear()
            queens = 0
            placementGrid = [[0 for _ in range(8)] for _ in range(8)]
            valid = [[False for _ in range(8)] for _ in range(8)]
            availableRows = {0, 1, 2, 3, 4, 5, 6, 7}
            availableCols = {0, 1, 2, 3, 4, 5, 6, 7}
    
    # If the row-column combination can allow for queen placement then create a key for its weight
    # in the weightToButtonMap dict, and a key for its colony in queensColonies dict
    if placementGrid[row][col] == 0:
        weightToButtonMap[(row, col)] = 0
        queensColonies[(row, col)] = set()

        # Add one to queens to get the total number of queens successfully placed
        queens += 1

        # Change the value of placementGrid[row][col] to 2 to represent the diagonals
        # touching a queen's block and 1 to represent the queen's designated column and row
        if row > 0 and col > 0:
            placementGrid[row-1][col-1] = 2
        if row > 0 and col < 7:
            placementGrid[row-1][col+1] = 2
        if row < 7 and col > 0:
            placementGrid[row+1][col-1] = 2
        if row < 7 and col < 7:
            placementGrid[row+1][col+1] = 2
        for j in range(8):
            placementGrid[row][j] = 1
            placementGrid[j][col] = 1
        
        valid[row][col] = True

        # Remove the row-column combination as viable options to place queens
        availableRows.remove(row)
        availableCols.remove(col)

queensAvailable = list(queensColonies.keys())
# Initialize an array to hold randomly generated area distributions on the grid
weights = assignAreaWeights(queens)

hint = tk.Button(app, width=20, height=2, bd=1, relief="solid", text="REVEAL A QUEEN!")
hint.config(command=revealQueen)
hint.pack(padx=10, pady=100)

# Assign each individual queen a weight that corresponds to the area of their colony
for (i, j) in zip(weightToButtonMap.keys(), weights):
    weightToButtonMap[i] = j

# Assign each queen a color and map out their colony with a random shape
for i in weightToButtonMap.keys():
    color = choice(islandColors)
    islandColors.remove(color)
    weight = [weightToButtonMap[i]-1]
    helper(i, grid, weight, color)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
discoveredColoniesQueue = deque()
visited = set()
        
# Add all uncolonized blocks to the nearest found colony
for i in range(8):
    for j in range(8):
        grid[i][j].config(command=lambda b=grid[i][j], x=i, y=j: drawX(b, x, y))
        shuffle(directions)
        if not valid[i][j]:
            nearestColony = helper2((i, j))
            newColor = grid[nearestColony[0]][nearestColony[1]].cget("bg")
            valid[i][j] = True
            grid[i][j].config(bg=newColor)

for i in queensColonies.keys():
    getColony(i)

            
app.mainloop()
