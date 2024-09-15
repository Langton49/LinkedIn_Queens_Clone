import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
from collections import deque

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

def checkColony(r, c):
    for i in queensColonies.keys():
        if (r, c) in queensColonies[i]:
            for t in queensColonies[i]:
                if t != (r, c) and grid[t[0]][t[1]]['text'] == "Q":
                    messagebox.showinfo("Alert", "There is already a queen in this colony!")
                    break
            break

def firstWinCondition():
    queens = 0
    totalQueens = len(queensColonies)
    for i in queensColonies.values():
        for t in i:
            if grid[t[0]][t[1]]['text'] == "Q":
                queens += 1
    return queens == totalQueens

def secondWinCondition():
    rowsSet = set()
    colsSet = set()
    if firstWinCondition():
        for i in queensColonies.values():
            for t in i:
                if grid[t[0]][t[1]]['text'] == "Q":
                    rowsSet.add(t[0])
                    colsSet.add(t[1])
        
        return len(rowsSet) == len(colsSet)
    return False

def thirdWinCondition():
    if secondWinCondition():
        for i in queensColonies.values():
            for t in i:
                if grid[t[0]][t[1]]['text'] == "Q":
                    if t[0]<7 and t[1]<7 and grid[t[0]+1][t[1]+1] == "Q":
                        return False
                    if t[0]<7 and t[1]>0 and grid[t[0]+1][t[1]-1] == "Q":
                        return False
                    if t[0]>0 and t[1]<7 and grid[t[0]-1][t[1]+1] == "Q":
                        return False
                    if t[0]>0 and t[1]>0 and grid[t[0]-1][t[1]-1] == "Q":
                        return False
        return True
    return False



def eliminateColony(r, c):
    for i in queensColonies.keys():
        if (r, c) in queensColonies[i]:
            for t in queensColonies[i]:
                if t != (r, c) and grid[t[0]][t[1]]['text'] != "Q":
                    grid[t[0]][t[1]].config(text="X")
            break

def clearColony(r, c):
    for i in queensColonies.keys():
        if (r, c) in queensColonies[i]:
            for t in queensColonies[i]:
                    if grid[t[0]][t[1]]['text'] != "Q":
                        grid[t[0]][t[1]].config(text="")
            break

def drawX(button, r, c):
    if button['text'] == "X":
        button.config(text="Q")
        eliminateColony(r, c)
        for i in range(8):
            if i != c and grid[r][i]['text'] == "Q":
                messagebox.showinfo("Alert", "Queen cannot go there")
                return
            elif i != c:
                grid[r][i].config(text="X")
        for i in range(8):
            if i != r and grid[i][c]['text'] == "Q":
                messagebox.showinfo("Alert", "Queen cannot go there")
                return
            elif i != r:
                grid[i][c].config(text="X")
        if (r>0 and c<7 and grid[r-1][c+1]['text'] == "Q") or (r<7 and c<7 and grid[r+1][c+1]['text'] == "Q") or (r>0 and c>0 and grid[r-1][c-1]['text'] == "Q") or (r<7 and c>0 and grid[r+1][c-1]['text'] == "Q"):
            messagebox.showinfo("Alert", "Queen cannot go there")
            return
        else:
            if r>0 and c<7:
                grid[r-1][c+1].config(text="X")
            if r<7 and c<7:
                grid[r+1][c+1].config(text="X")
            if r>0 and c>0:
                grid[r-1][c-1].config(text="X")
            if r<7 and c>0:
                grid[r+1][c-1].config(text="X")
        checkColony(r, c)
        if thirdWinCondition():
            messagebox.showinfo("Congratulations", "You have won!")
            return
        
    elif button['text'] == "Q":
        button.config(text="")
        for i in range(8):
            grid[r][i].config(text="")
            grid[i][c].config(text="")
        if r>0 and c<7:
            grid[r-1][c+1].config(text="")
        if r<7 and c<7:
            grid[r+1][c+1].config(text="")
        if r>0 and c>0:
            grid[r-1][c-1].config(text="")
        if r<7 and c>0:
            grid[r+1][c-1].config(text="")
        clearColony(r, c)
    else:
        button.config(text="X")


valid = [[False for _ in range(8)] for _ in range(8)]
islandColors = ['red', 'green', 'aliceblue', 'yellow', 'cyan', 'deeppink', 'violet', 'orange', 'seagreen1']

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

app = tk.Tk()
app.title("Queens")
app.geometry("700x700")

frame = tk.Frame(app)
frame.place(rely=0.5, relx=0.5, anchor="center")

grid = []
for i in range(8):
    rows = []
    for j in range(8):
        newButton = tk.Button(frame, width=5, height=2, bd=1, relief="solid")
        newButton.grid(row=i, column=j, sticky="nsew")
        rows.append(newButton)
    grid.append(rows)

booleanGrid = [[0 for _ in range(8)] for _ in range(8)]  

availableRows = {0, 1, 2, 3, 4, 5, 6, 7}
availableCols = {0, 1, 2, 3, 4, 5, 6, 7}
queens = 0
weightToButtonMap = {}
queensColonies = {}

while availableCols:
    rList = list(availableRows)
    cList = list(availableCols)
    row = choice(rList)
    col = choice(cList)
    if len(rList) == 1:
        if booleanGrid[row][col]:
            break
    if booleanGrid[row][col] == 0:
        weightToButtonMap[(row, col)] = 0
        queensColonies[(row, col)] = set()
        queens += 1
        booleanGrid[row][col] = 3
        if row > 0 and col > 0:
            booleanGrid[row-1][col-1] = 2
        if row > 0 and col < 7:
            booleanGrid[row-1][col+1] = 2
        if row < 7 and col > 0:
            booleanGrid[row+1][col-1] = 2
        if row < 7 and col < 7:
            booleanGrid[row+1][col+1] = 2
        for j in range(8):
            booleanGrid[row][j] = 1
            booleanGrid[j][col] = 1
        #grid[row][col].config(text="Q")
        valid[row][col] = True
        availableRows.remove(row)
        availableCols.remove(col)

weights = assignAreaWeights(queens)
for (i, j) in zip(weightToButtonMap.keys(), weights):
    weightToButtonMap[i] = j

for i in weightToButtonMap.keys():
    color = choice(islandColors)
    islandColors.remove(color)
    weight = [weightToButtonMap[i]-1]
    helper(i, grid, weight, color)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
discoveredColoniesQueue = deque()
visited = set()
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
        

for i in range(8):
    for j in range(8):
        grid[i][j].config(command=lambda b=grid[i][j], x=i, y=j: drawX(b, x, y))
        shuffle(directions)
        if not valid[i][j]:
            nearestColony = helper2((i, j))
            newColor = grid[nearestColony[0]][nearestColony[1]].cget("bg")
            valid[i][j] = True
            grid[i][j].config(bg=newColor)

def getColony(queen):
    colonyColor = grid[queen[0]][queen[1]].cget("bg")
    for i in range(8):
        for j in range(8):
            if grid[i][j].cget("bg") == colonyColor:
                queensColonies[queen].add((i, j))
            
# for i in queensColonies.keys():
#     getColony(i)
#     print(i, "--->", queensColonies[i], end="\n")

app.mainloop()

