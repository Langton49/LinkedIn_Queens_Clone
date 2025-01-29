# LinkedIn Queens Clone 👑

## Table of Contents 📑
1. [Overview](#overview)
2. [How I Made It](#how-i-made-it)
   1. [Technology Stack](#technology-stack)
   2. [Development Approach](#development-approach)
      - [Generating Unique Colony Shapes](#generating-unique-colony-shapes)
      - [Assigning Colonies to Queens](#assigning-colonies-to-queens)
      - [Making the Game Interactive](#making-the-game-interactive)
      - [Additional Features](#additional-features)
4. [How To Run It](#how-to-run-it)
5. [DEMO](#demo)
6. [Contributing](#contributing)
7. [Contact](#contact)

## Overview 📃 <a name="overview">
One of my favorite parts about LinkedIn is the daily in-stream puzzle games that were introduced back in May 2024. My favorite of all of these games is Queens. In Queens, you have to place queens into different areas of a square with the following rules.

- Each queen must occupy a unique colored area on the square grid.
- No two queens can share the same row or column.
- Queens may not touch each other diagonally.

The square can contain an arbitrary number of rows and columns so there can be any number of queens per puzzle. The puzzle is never the same and the shapes of each area is always different from one puzzle to the next.\
\
__📼 If you've never played it here is a short clip:__\
\
![alt text](https://github.com/Langton49/LinkedIn_Queens_Clone/blob/main/Assets/14-49-29.gif "An Example of a LinkedIn Queens Puzzle")

GIF Made With: [Free Convert](https://www.freeconvert.com/)

### Why I made this
As I played, I became curious about how LinkedIn might generate fresh puzzles daily.My hypothesis: LinkedIn uses procedural generation to create each puzzle. I reached out to some
 engineers at LinkedIn but they never got back to me. Unable to confirm this, I decided to test my theory by building my own version of the game. This project is my attempt to recreate the puzzle logic and design a game where players can interact with dynamically generated grids.
 
## How I made it 🔨 <a name="how-i-made-it">
### Technology Stack <a name="technology-stack">
- Python (version 3.12.4)
- Tkinter (version 8.6)

### Development Approach <a name="development-approach">
Approaching this problem I imagined each queen as the monarch of different colonies on the gameboard. The biggest questions I had were: 
1. How to create different shapes for each colony for each game session?
2. How I could assign different colonies of the square to each queen?
3. How to make the UI respond to user actions?

#### Generating Unique Colony Shapes <a name="generating-unique-colony-shapes">
To create different colonies for each game session, it would have to use randomness in a way that would limit each colony to the gameboard. The game board is an 8x8
square made up of 1x1 tkinter button objects (I decided to limit the gameboard to this size for the time being so I could create 
a minimum viable product). So if we are working with colonies, the land area is 64 square units where a single unit is a single button. I needed to divide this area between 8 queens per game session 
(Recall to solve the puzzle, each queen must be in it's own row and column. 8 rows, 8 columns, 8 queens) hence I needed 8 colonies.\
\
I decided to assign 'weights' to each colony before creating them. The weights would represent the portion of the total land area each queen would own. Then, using a random walk, I mapped out the shapes of each colony according to their weights. I adjusted for visited buttons and buttons that were already assigned to other colonies. However, because its a random walk there would sometimes be holes (The random walk, walked in a circle and left a block or two unassigned in the middle of a colony). I fixed this by allowing all possible buttons to be assigned and then looped through all of them to find any unassigned buttons. If unassigned buttons were found they would be assigned to the colony closest to them, found using a breadth first search (The drawbacks are that sometimes there is a really large area with many small areas and sometimes there are colonies with one assigned button for an area although the weight assignment was made to ensure the minimum area of any colony is 2 square units). To mark the colonies I used the value of the bg-color property of the tkinter buttons as an indicator that a button belongs to a specific colony.

#### Assigning Colonies to Queens <a name="assigning-colonies-to-queens">
To assign the different colonies to the queens I assigned the location (button) where each queen would be beforehand (its the first function that runs before assigning weights). Then I used a dictionary, with the coordinates of the button in a tuple as the key, to store a mapping from the queen to every button that is apart of its colony, added according to the value of their bg-color after each area was assigned.

#### Making the Game Interactive <a name="making-the-game-interactive">
To make the UI responsive with user actions, I used an 8x8 integer matrix to keep track of where the user had performed specific actions. Actions include: placing a queen, eliminating a block by placing a cross and removing a queen. Each user action would change the value of different buttons depending on what the user does. For example, when a user places a queen by double clicking, the colony into which that queen is placed is 'eliminated' (crosses are placed on all buttons in the colony). Internally, the program checks which colony the queen is placed in and increments the corresponding values in the integer matrix for all buttons within that colony.

#### Additional Features <a name="additional-features">
Once the main game components were achieved I went ahead and added other parts of the program, focusing mainly on the UI, game logic and helper functions to support the gameplay. I also added a hint button similar to the one in the original game with the difference being that this button instead of give shallow clues, simply revealed one the queens on the gameboard. 

## How To Run It🤷‍♂️ <a name="how-to-run-it">
### Requirements:
1. If you have not already, [install Python](https://www.python.org/downloads/) (3.12.4 or later)
2. If you have not already, install tkinter (8.6 or later)
```bash
pip install tkinter
```

### Running The Program
1. Clone this repo:
```bash
git clone https://github.com/Langton49/LinkedIn_Queens_Clone.git
```
2. Navigate to the `source` folder.
3. Open a terminal in that directory and type the following command:
```bash
python LinkedIn_Queens_Clone.py
```
OR
```bash
python3 LinkedIn_Queens_Clone.py
```
Ensure you are in the source folder's directory.
4. You should now be able to see the game window and play the game.


## DEMO 🎞 <a name="demo">
\
![alt text](https://github.com/Langton49/LinkedIn_Queens_Clone/blob/main/Assets/14-57-38.gif "An Example of a LinkedIn Queens Puzzle")

GIF Made With: [Free Convert](https://www.freeconvert.com/)

## Contributing 🤝 <a name="contributing">
Because software development is an ongoing and collaborative process, contributions are welcome. Simply create a branch, commit your changes, push to the branch and open a pull request.

## Contact ✉ <a name="contact">
__Author:__ Munashe Mukweya\
__Email:__ munashemukweya2022@gmail.com\
__GitHub:__ https://github.com/Langton49



