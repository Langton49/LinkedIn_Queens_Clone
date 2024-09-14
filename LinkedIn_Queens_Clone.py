import tkinter as tk
from random import randint, choice, shuffle

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


valid = [[False for _ in range(8)] for _ in range(8)]
islandColors = ['red', 'green', 'blue', 'yellow', 'cyan', 'deeppink', 'violet', 'orange', 'seagreen1']

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

frame = tk.Frame(app, bd=2, relief="solid", highlightbackground="red", highlightthickness=2)
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
        grid[row][col].config(text="Q")
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

print(weightToButtonMap)
            

app.mainloop()

