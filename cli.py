import sys

class Message:
  '''Contains all the messages displayed to the user.'''
  def __init__(self):
    pass
  def welcome(self):
    message = (f"Welcome to command-line Connect 4, powered by Python.\n" 
      f"Start by selecting a difficulty level (easy, medium or hard) for your computer opponent.\n"
      f"Next the system will randomly select which player goes first.\n"
      f"On your turn, make your move by inputting the column number (from 0 - 6) "
      f"where you wish to go.\n"
      f"The updated board will display after each move.\n"
      f"The winner is the first player to connect 4 of their pieces horizontally, "
      f"vertically, or diagonally.\n"
      f"Ready? Let's get started.\n")
    return message 
  def exit_errors(self):
    return("Exiting the game due to too many errors.")
  def difficulty_prompt(self):
    return("Select a difficulty level: ")
  def difficulty_error(self):
    return("Error: Please provide a valid difficulty level.")
  def move_prompt(self):
    return("Make your move: ")
  def move_error(self):
    return("Error: Please enter a valid column number.")
  def human_is(self, player):
    return(f"You are {player}")
  def computers_move(self):
    return("Computer's move")
  def winner(self, player):
    return(f"Winner: {player}")
  def tie(self):
    return("Tie game")
  def thanks(self):
    return("Thanks for playing. To start a new game, run the script again.")  

class CLI:
  '''Controls operations to receive input from the user on the command line 
  (to set the difficulty level and make a move), handling errors appropriately.
  Also prints out the current state of the game board, and messages for the end
  of the game.'''
  def __init__(self):
    pass
  def begin(self):
    print(Message().welcome())
  def input_difficulty(self):
    # prompt the user to choose the difficulty level of the AI. Any valid string
    # beginning with 'e' (easy), 'm' (medium), or 'h' (hard) is accepted
    # try 10 times then give up
    for _ in range(10):
      difficulty = input(Message().difficulty_prompt())
      if not difficulty or difficulty[0].upper() not in ['E', 'M', 'H']:
        print(Message().difficulty_error())
      else:
        return difficulty[0].upper()
    print(Message().exit_errors())
    sys.exit()    
  def input_move(self):
    # prompt the user to select the column to place their checker in. Column numbers
    # 0 - 6 are accepted
    # try 10 times then give up
    for _ in range(10):
      try:
        move = int(input(Message().move_prompt()))
      except ValueError:
        print(Message().move_error())
      else:
        if move >= 0 and move <= 6:
          return move 
        else:
          print(Message().move_error())
    print(Message().exit_errors())
    sys.exit()
  def output_board(self, board):
    print("_"*28)
    for col in board:
      print(f"| {' | '.join(col)} |")
    print("¯"*28)
    print("  0   1   2   3   4   5   6")
  def human_is(self, player):
    print(Message().human_is(player))
  def computers_move(self):
    print(Message().computers_move())
  def end_winner(self, player):
    print(Message().winner(player))
  def end_tie(self):
    print(Message().tie())
  def thanks(self):
    print(Message().thanks())  