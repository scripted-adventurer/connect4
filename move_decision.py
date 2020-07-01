import random
import itertools

class MoveDecisionBase:
  '''The nase class to inherit from. All inherited classes should take the current
  game board as input and provide a move() method to output the computer's move.'''
  def __init__(self, board):
    self.board = board
    self.available_moves = []
    self.get_available_moves()
  def get_available_moves(self):
    # find the (row, column) index pair for the open slot of each non-full column
    for column in range(7):
      available = None
      for row in range(6):
        if self.board[row][column] == ' ':
          available = (row, column)
        else:
          break
      if available:
        self.available_moves.append(available)      
  def move(self):
    # override this method
    pass  

class MoveDecisionEasy(MoveDecisionBase):
  '''Contains the logic for the computer player when set to 'easy' difficulty.
  Simply collects the list of available moves and makes a random one.'''
  def __init__(self, board):
    super().__init__(board)
  def move(self):
    return random.choice([move[1] for move in self.available_moves])

class MoveDecisionMedium(MoveDecisionBase):
  ''' '''
  def __init__(self, board):
    super().__init__(board)
  def _empty_board(self):
    for row, column in itertools.product(range(6), range(7)):
      if self.board[row][column] != ' ':
        return False
    return True
  def _computer_player_1(self):
    # if there are an even number of moves on the board, the computer is player 1
    total_pieces = 0
    for row, column in itertools.product(range(6), range(7)):
      if self.board[row][column] != ' ':
        total_pieces += 1
    player_1 = True if total_pieces % 2 == 0 else False    
    return player_1
  def _score_direction(self, direction, start_row, start_column):
    # calculate each direction's score for both players
    # check for nonexistent rows 
    if start_row < 0 or start_column < 0:
      return (0, 0)
    
    player_1_score = 0
    player_2_score = 0
    if direction == 'vertical':
      rows = range(start_row, 6)
      columns = [start_column]
      points = itertools.product(rows, columns)
    if direction == 'horizontal_left':
      rows = [start_row]
      columns = range(start_column, -1, -1)
      points = itertools.product(rows, columns)
    if direction == 'horizontal_right':
      rows = [start_row]
      columns = range(start_column, 7)
      points = itertools.product(rows, columns)
    if direction == 'diagonal_NE_left':
      rows = range(start_row, 6)
      columns = range(start_column, -1, -1)
      total_points = min([len(rows), len(columns)])
      points = [(rows[x], columns[x]) for x in range(total_points)]
    if direction == 'diagonal_NE_right':
      rows = range(start_row, -1, -1)
      columns = range(start_column, 7)
      total_points = min([len(rows), len(columns)])
      points = [(rows[x], columns[x]) for x in range(total_points)]
    if direction == 'diagonal_SE_left':
      rows = range(start_row, -1, -1)
      columns = range(start_column, -1, -1)
      total_points = min([len(rows), len(columns)])
      points = [(rows[x], columns[x]) for x in range(total_points)]
    if direction == 'diagonal_SE_right':
      rows = range(start_row, 6)
      columns = range(start_column, 7)
      total_points = min([len(rows), len(columns)])
      points = [(rows[x], columns[x]) for x in range(total_points)]   
    
    for row, column in points:
      if self.board[row][column] == self.board[start_row][start_column]:
        if self.board[start_row][start_column] == 'X':
          player_1_score += 1
        elif self.board[start_row][start_column] == 'O':
          player_2_score += 1
      else:
        break 
    
    return (player_1_score, player_2_score)    
  def _score_position(self, row, column):
    # For each direction and player, find the number of that player's pieces 
    # directly connected to this board slot 
    score = {'p1_vertical': 0, 'p1_horizontal': 0, 'p1_diagonal_NE': 0, 
      'p1_diagonal_SE': 0, 'p2_vertical': 0, 'p2_horizontal': 0, 
      'p2_diagonal_NE': 0, 'p2_diagonal_SE': 0}
    
    vertical = self._score_direction('vertical', (row + 1), column)
    score['p1_vertical'] += vertical[0]
    score['p2_vertical'] += vertical[1]
    
    horizontal_left = self._score_direction('horizontal_left', row, (column - 1))
    score['p1_horizontal'] += horizontal_left[0]
    score['p2_horizontal'] += horizontal_left[1]
    
    horizontal_right = self._score_direction('horizontal_right', row, (column + 1))
    score['p1_horizontal'] += horizontal_right[0]
    score['p2_horizontal'] += horizontal_right[1]

    diagonal_NE_left = self._score_direction('diagonal_NE_left', (row + 1), 
      (column - 1))
    score['p1_diagonal_NE'] += diagonal_NE_left[0]
    score['p2_diagonal_NE'] += diagonal_NE_left[1]

    diagonal_NE_right = self._score_direction('diagonal_NE_right', (row - 1), 
      (column + 1))
    score['p1_diagonal_NE'] += diagonal_NE_right[0]
    score['p2_diagonal_NE'] += diagonal_NE_right[1]
    
    diagonal_SE_left = self._score_direction('diagonal_SE_left', (row - 1), 
      (column - 1))
    score['p1_diagonal_SE'] += diagonal_SE_left[0]
    score['p2_diagonal_SE'] += diagonal_SE_left[1]

    diagonal_SE_right = self._score_direction('diagonal_SE_right', (row + 1), 
      (column + 1))
    score['p1_diagonal_SE'] += diagonal_SE_right[0]
    score['p2_diagonal_SE'] += diagonal_SE_right[1]
    
    return score 
  def move(self):
    # select a move based on the decision logic (see README for details)
    if self._empty_board():
      return 3

    player_1 = self._computer_player_1()  
    winning_move = None
    game_saving_move = None
    highest_score = -1
    highest_score_move = None
    for row, column in self.available_moves:
      slot_sum = 0
      for direction, count in self._score_position(row, column).items():
        slot_sum += count 
        if count >= 3:
          if ((player_1 and direction[:2] == 'p1') or 
            (not player_1 and direction[:2] == 'p2')):
            winning_move = (row, column)
          else:
            game_saving_move = (row, column)
      if slot_sum > highest_score:
        highest_score = slot_sum
        highest_score_move = (row, column)
      # break ties by selecting the column closer to the center 
      elif (slot_sum == highest_score and 
        abs(3 - column) < abs(3 - highest_score_move[1])):
        highest_score_move = (row, column)        

    if winning_move:
      return winning_move[1]
    elif game_saving_move:
      return game_saving_move[1]
    else:
      return highest_score_move[1]     

class MoveDecisionHard(MoveDecisionBase):
  ''' '''
  def __init__(self, board):
    super().__init__(board) 
  def move(self):
    return 0     