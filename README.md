# Connect Four #

A simple, command line based package to simulate player vs. computer games of Connect Four. 

## Gameplay ##

All user interaction occurs through the terminal window. After running the script, you will be prompted to select a difficulty level (easy, medium, or hard). Then the script will randomly assign either the human player or the computer to go first. After each move, the updated board will be displayed in the terminal window. The game ends when either player successfully connects four of their own pieces on the gameboard (either vertically, horizontally, or diagonally.)

## How It Works ##

The game's three levels of computer player difficulty are based on three separate move decision algorithms. 

### Easy ###

This level uses an incredibly simple algorithm: given all the available moves, choose one randomly. 

### Medium ###

This level uses a more nuanced decision making hierarchy. Each potential move (of which there are at maximum 7, corresponding to the 7 columns of the game board) is assigned a multi dimensional score based on the count of different groupings of pieces attached to that slot (evaluating horizontal, vertical, and diagonal groupings - in other words, all the ways to win):
1. Three of the computer's pieces. Going here will win the game for the computer.
2. Three of the human player's pieces. Going here will prevent a win by the human player. 
3. Two of the computer's pieces. 
4. Two of the opponent's pieces.
5. One of the computer's pieces. 

The slot with the highest score at level 1 is selected. Ties are broken by the scores at subsequent levels. If two slots have the exact same score from all levels, one is selected randomly. 

### Hard ###

*In progress*