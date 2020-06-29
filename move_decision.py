import random

class MoveDecisionBase:
  '''The nase class to inherit from. All inherited classes should take the current
  game board as input and provide a move() method to output the computer's move.'''
  def __init__(self, board):
    self.board = board
    self.available_moves = []
  def get_available_moves(self):
    # find the indexes of columns that are not full and can be played in
    for column in range(7):
      if self.board[0][column] == ' ':
        self.available_moves.append(column) 
  def move(self):
    # override this method
    pass  

class MoveDecisionEasy(MoveDecisionBase):
  '''Contains the logic for the computer player when set to 'easy' difficulty.
  Simply collects the list of available moves and makes a random one.'''
  def __init__(self, board):
    super().__init__(board)
  def move(self):
    self.get_available_moves()
    return random.choice(self.available_moves)

class MoveDecisionMedium(MoveDecisionBase):
  ''' '''
  def __init__(self, board):
    super().__init__(board)
  def move(self):
    return 0

class MoveDecisionHard(MoveDecisionBase):
  ''' '''
  def __init__(self, board):
    super().__init__(board)
  def move(self):
    return 0     