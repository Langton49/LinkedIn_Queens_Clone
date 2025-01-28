# LinkedIn Queens Clone 👑
## Overview
One of my favorite parts about LinkedIn is the daily in-stream puzzle games that were added back in May 2024. I wake up every morning and keep my streak up 
before I do anything else and my favorite of all of these games is Queens. In Queens, you have to place queens into different areas of a square with the following rules.

- There should be one queen in each colored area inside a square.
- There cannot be two queens in the same row or column.
- The queens may not touch each other diagonally.

The square can contain an arbitrary number of colored areas so there can be any number of queens per puzzle. The puzzle is never the same and the shapes of each area is always different from one puzzle to the next.\
\
__📼 If you've never played it here is a short clip:__\
\
![alt text](https://github.com/Langton49/LinkedIn_Queens_Clone/blob/main/Assets/14-49-29.gif "An Example of a LinkedIn Queens Puzzle")

GIF Made With: [Free Convert](https://www.freeconvert.com/)

### Why I made this
One day as I was playing, I wondered how LinkedIn managed to generate different puzzles everyday. My thought was it may be a complex algorithm that proceduarally generates each puzzle day after day. I asked some
 employees at LinkedIn but they never got back to me so I decided to try to prove that that was how they were doing it by making my own implementation. 

## How I made it
### Technology
- Python (version 3.12.4)
- Tkinter (version 8.6)

### Implementation
Approaching this problem I imagined each queen as the monarch of different colonies on the gameboard. The biggest questions I had were: 
1. How to create different shapes for each colony for each game session?
2. How I could assign different colonies of the square to each queen?
3. How to make the UI respond to user actions?

#### Question 1
To create different colonies for each game session, it would have to use randomness in a way that would limit each colony to the gameboard. The game board is an 8x8
square made up of 1x1 tkinter button objects (I decided to limit the gameboard to this size for the time being so I could create 
a minimum viable product). So if we are working with colonies, the land area is 64 square units where a single unit is a single button. I needed to divide this area between 8 queens per game session 
(Recall to solve the puzzle, each queen must be in it's own row and column. 8 rows, 8 columns, 8 queens) hence I needed 8 colonies. I decided to assign 'weights' to each colony before creating them. The
weights would represent the portion of the total land area each queen would own. Then, using a random walk, I mapped out the shapes of each colony according to their weights. I adjusted for visited buttons
and buttons that were already assigned to other colonies. However because its a random walk, there would sometimes be holes (The random walk, walked in a circle and left a block or two unassigned). I fixed this by allowing all possible buttons be assigned and then looped through all buttons to find any unassigned buttons. If unassigned buttons were found they would be assigned the colony closest to them found using a
breadth first search (The drawbacks are that sometimes there is a really large area with many small areas and sometimes there are colonies with one assigned area although the weight assignment was made to ensure
the minimum area of any colony is 2 square units). To mark the colonies I used the value of the bg-color property of the tkinter buttons.

#### Question 2
To assign the different colonies to the queens I assigned the location (button) where each queen would be. Then I used a dictionary, with the coordinates of the button in a tuple as the key, to store a mapping
from the queen, to every button that is apart of its colony added according to the value of their bg-color after each area was assigned.

#### Question 3
To make the UI responsive with user actions, I used an 8x8 integer matrix to keep track of where the user had performed specific actions. Actions include: placing a queen, eliminating a block by placing a cross and removing a queen. Each user action would change the value of different buttons depending on what the user does. For example, when a user places a queen by double clicking, the colony into which that queen is place is 'eliminated' (crosses are placed on all buttons in the colony). Internally, there is a check to see which colony the queen was placed and to add 1 to the integer matrix to all numbers with the same assigned coordinates.

#### Everything Else
Once the main game components were achieved I went ahead and coded other parts of the program, such as win conditions, helper functions, and a button to reveal a queen on the gameboard.

## How To Run
1. Clone this repo:
```bash
git clone https://github.com/Langton49/LinkedIn_Queens_Clone.git
```
2. Navigate to the `source` folder.
3. Open a terminal in that directory and type the following command:
```console
python LinkedIn_Queens_Clone.py
```
OR
```console
python3 LinkedIn_Queens_Clone.py
```
Ensure you are in the source folder's directory.
4. You should now be able to see the game window and play the game.
\

__🎞 DEMO:__\
\
![alt text](https://github.com/Langton49/LinkedIn_Queens_Clone/blob/main/Assets/14-57-38.gif "An Example of a LinkedIn Queens Puzzle")

GIF Made With: [Free Convert](https://www.freeconvert.com/)

## Contributing
Because software development is an ongoing and collaborative process, contributions are welcome. Simply create a branch, commit your changes, push to the branch and open a pull request.

## Contact
__Author:__ Munashe Mukweya\
__Email:__ munashemukweya2022@gmail.com\
__GitHub:__ https://github.com/Langton49



