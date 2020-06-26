import itertools 

class Board:
  '''Logically represents the board used in gameplay, including methods to make a
  move and check for a winner.'''
  def __init__(self):
    self.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
  def move(self, column, player1):
    # place the piece in the column in the first empty slot from the bottom
    # return True if successful, False if the column is full
    if player1:
      piece = 'X'
    else:
      piece = 'O'
    for row in range(5, -1, -1):
      if self.board[row][column] == ' ':
        self.board[row][column] = piece
        return True
    return False
  def _horizontal_winner(self, row, column):
    # check if there is a horizontal connect 4 to the right (higher column) from here
    # skip checking columns 4 - 6 as any connect 4 here would be captured earlier
    if column > 3:
      return False
    if (self.board[row][column] != ' ' and 
      self.board[row][column] == self.board[row][column + 1] and 
      self.board[row][column] == self.board[row][column + 2] and 
      self.board[row][column] == self.board[row][column + 3]):
      return True
    else:
      return False  
  def _vertical_winner(self, row, column):
    # check if there is a vertical connect 4 up (lower row) from here
    # skip checking rows 0 - 2 as any connect 4 here would be captured earlier
    if row < 3:
      return False
    if (self.board[row][column] != ' ' and 
      self.board[row][column] == self.board[row - 1][column] and 
      self.board[row][column] == self.board[row - 2][column] and 
      self.board[row][column] == self.board[row - 3][column]):
      return True
    else:
      return False  
  def _diagonal_up_winner(self, row, column):
    # check if there is a diagonal connect 4 up and to the right from here
    # skip rows 0 - 2 and columns 4 - 6 as up-right diagonals are not possible from there 
    if row < 3 or column > 3:
      return False 
    if (self.board[row][column] != ' ' and 
      self.board[row][column] == self.board[row - 1][column + 1] and 
      self.board[row][column] == self.board[row - 2][column + 2] and 
      self.board[row][column] == self.board[row - 3][column + 3]):
      return True
    else:
      return False 
  def _diagonal_down_winner(self, row, column):
    # check if there is a diagonal connect 4 down and to the right from here
    # skip rows 0 - 2 and columns 4 - 6 as down-right diagonals are not possible from there 
    if row >= 3 or column > 3:
      return False 
    if (self.board[row][column] != ' ' and 
      self.board[row][column] == self.board[row + 1][column + 1] and 
      self.board[row][column] == self.board[row + 2][column + 2] and 
      self.board[row][column] == self.board[row + 3][column + 3]):
      return True
    else:
      return False 
  def check_winner(self):
    # search bottom (highest row) to top, left (lowest column) to right 
    rows = range(5, -1, -1)
    columns = range(7)
    for row, column in itertools.product(rows, columns):
      if (self._horizontal_winner(row, column) or self._vertical_winner(row, column) 
        or self._diagonal_up_winner(row, column) or 
        self._diagonal_down_winner(row, column)):
        return True
    return False     
  def get_board(self):
    return self.board  