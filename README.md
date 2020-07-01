# Connect Four #

A simple, command line based package to simulate player vs. computer games of Connect Four. 

## Gameplay ##

All user interaction occurs through the terminal window. After running the script, you will be prompted to select a difficulty level (easy, medium, or hard). Then the script will randomly assign either the human player or the computer to go first. After each move, the updated board will be displayed in the terminal window. The game ends when either player successfully connects four of their own pieces on the gameboard (either vertically, horizontally, or diagonally.)

## How It Works ##

The game's three levels of computer player difficulty are based on three separate move decision algorithms. 

### Easy ###

This level uses an incredibly simple algorithm: given all the available moves, choose one randomly. 

### Medium ###

This level uses a more nuanced decision making hierarchy. 

If the computer is player 1, go in the middle at the start of the game. Connect 4 is a solved game, and analysis shows that this move is most advantageous. 

For any other move, evaluate each potential board slot (of which there are at maximum 7, corresponding to the 7 columns of the game board) by finding, in each direction, the number of each player's pieces that are directly connected to the slot.

This score table looks like this:

```
{'p1_vertical': 0, 'p1_horizontal': 0, 'p1_diagonal_up': 0, 'p1_diagonal_down': 0, 'p2_vertical': 0, 'p2_horizontal': 0, 'p2_diagonal_up': 0, 'p1_diagonal_down': 0}
```

As an example, consider the following game board:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   | X |
|   | X |   | O | O |   | O |
| X | O |   | X | X |   | X |
| O | X |   | X | O |   | O |
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
  0   1   2   3   4   5   6
```  

Here X is player 1, and O is player 2. If the computer were evaluating column 2:
* p1_vertical and p2_vertical are both 0, as there are no pieces below the slot.
* p1_horizontal is 2, as there is one X piece to the left and one X piece to the right of the slot. 
* p2_horizontal is 0, as there are no O pieces to the left or the right of the slot. 
* p1_diagonal_NE is 1, as there is one X piece on a northeast/southwest line from the slot.
* p1_diagonal_SE is 0, as there are no X pieces on a southeast/northwest line from the slot.
* p2_diagonal_NE is 0, as there are no O pieces on a northeast/southwest line from the slot.
* p2_diagonal_SE is 1, as there is one O pieces on a southeast/northwest line from the slot.

Then each move is considered and the following decision making algorithm is applied:
* If any potential move has any score of 3+ for the computer player, select that move. (This will win the game.)
* If any potential move has a score of 3+ for the human player, select that move. (This will prevent the human player from winning on the next turn.)
* Otherwise, find the move with the highest sum across all dimensions of the score. Ties are broken by selecting the move closest to the middle of the board. 

This approach results in play that seeks to build up chains of the computer's own pieces and block chains of the human player's pieces.

### Hard ###

*In progress*