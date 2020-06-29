import unittest
import unittest.mock
import sys
import itertools
import copy 

from board import Board
from cli import CLI
from move_decision import MoveDecisionBase, MoveDecisionEasy

class TestIO(unittest.TestCase):

  def setUp(self):
    self.cli = CLI()

  def test_input_difficulty(self):
    # map each valid input to its expected output
    valid_data = {}
    for level in ['Easy', 'Medium', 'Hard']:
      value = level[0]
      valid_data[level] = value
      valid_data[level.upper()] = value
      valid_data[level.lower()] = value
      valid_data[level[0]] = value
      valid_data[level[0].lower()] = value
    for input_str, return_val in valid_data.items():
      with unittest.mock.patch('builtins.input', return_value=input_str):
        self.assertEqual(self.cli.input_difficulty(), return_val)
    invalid_data = iter(['', 'a', ' ', '\n', 0, 'xyz', '5', '$', '__', 'v'])
    with unittest.mock.patch('builtins.input', return_value=next(invalid_data)):
      self.assertRaises(SystemExit, self.cli.input_difficulty)
  def test_input_move(self):
    valid_data = ['0', '1', '2', '3', '4', '5', '6']
    for input_str in valid_data:
      with unittest.mock.patch('builtins.input', return_value=input_str):
        self.assertEqual(self.cli.input_move(), int(input_str))
    invalid_data = iter(['', 'a', ' ', '\n', 'three', 'z', '$', '_', '+', 'wetw4t4'])
    with unittest.mock.patch('builtins.input', return_value=next(invalid_data)):
      self.assertRaises(SystemExit, self.cli.input_move)
  def test_output_board(self):
    empty_board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    self.cli.output_board(empty_board)
    full_board = [
      ['O', 'O', 'O', 'X', 'O', 'O', 'X'],
      ['X', 'X', 'X', 'O', 'X', 'X', 'O'],
      ['O', 'X', 'O', 'O', 'X', 'X', 'X'],
      ['O', 'O', 'X', 'O', 'X', 'O', 'O'],
      ['O', 'X', 'O', 'X', 'O', 'X', 'X'],
      ['X', 'O', 'X', 'X', 'O', 'X', 'O']
    ]
    self.cli.output_board(full_board)
  def test_messages(self):
    self.cli.human_is('player 1')
    self.cli.human_is('player 2')
    self.cli.computers_move()
    self.cli.end_winner('Player 1')
    self.cli.end_winner('Player 2')
    self.cli.end_tie()
    self.cli.thanks()  
           
class TestBoard(unittest.TestCase):

  def setUp(self):
    self.board = Board()
    self.empty_board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '] ]

  def test_move(self):
    self.assertEqual(self.board.move(column=3, player1=True), True)
    self.assertEqual(self.board.move(column=4, player1=False), True)
    self.assertEqual(self.board.move(column=4, player1=True), True)
    self.assertEqual(self.board.move(column=3, player1=False), True)
    self.assertEqual(self.board.move(column=2, player1=True), True)
    self.assertEqual(self.board.move(column=1, player1=False), True)
    self.assertEqual(self.board.move(column=2, player1=True), True)
    self.assertEqual(self.board.move(column=4, player1=False), True)
    self.assertEqual(self.board.move(column=2, player1=True), True)
    self.assertEqual(self.board.move(column=2, player1=False), True)
    self.assertEqual(self.board.get_board(), [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', 'O', ' ', ' ', ' ', ' '],
      [' ', ' ', 'X', ' ', 'O', ' ', ' '],
      [' ', ' ', 'X', 'O', 'X', ' ', ' '],
      [' ', 'O', 'X', 'X', 'O', ' ', ' ']
    ])
    self.assertEqual(self.board.move(column=2, player1=True), True)
    self.assertEqual(self.board.move(column=2, player1=False), True) 
    # full column test
    self.assertEqual(self.board.move(column=2, player1=True), False)
    self.assertEqual(self.board.move(column=2, player1=False), False)
    self.assertEqual(self.board.get_board(), [
      [' ', ' ', 'O', ' ', ' ', ' ', ' '],
      [' ', ' ', 'X', ' ', ' ', ' ', ' '],
      [' ', ' ', 'O', ' ', ' ', ' ', ' '],
      [' ', ' ', 'X', ' ', 'O', ' ', ' '],
      [' ', ' ', 'X', 'O', 'X', ' ', ' '],
      [' ', 'O', 'X', 'X', 'O', ' ', ' ']
    ])

  def test_end_of_game(self):
    # no winners
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '] ]
    self.assertEqual(self.board.end_of_game(), (False, ''))
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', 'X', 'O', ' ', ' ', ' ', ' '],
      [' ', 'O', 'O', 'X', 'O', ' ', ' '],
      [' ', 'X', 'X', 'O', 'X', 'O', ' '],
      [' ', 'O', 'X', 'X', 'O', 'X', ' '] ]
    self.assertEqual(self.board.end_of_game(), (False, ''))
    self.board.board = [
      ['X', 'O', ' ', 'X', ' ', ' ', 'O'],
      ['X', 'X', ' ', 'O', ' ', 'X', 'X'],
      ['X', 'O', ' ', 'O', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'O', 'X', 'X', 'X'],
      ['X', 'X', 'O', 'X', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'X', 'O', 'X', 'X'] ]
    self.assertEqual(self.board.end_of_game(), (False, ''))
    self.board.board = [
      ['X', 'O', 'X', 'X', 'O', 'X', 'O'],
      ['X', 'X', 'O', 'O', 'O', 'X', 'X'],
      ['X', 'O', 'X', 'O', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'O', 'X', 'X', 'X'],
      ['X', 'X', 'O', 'X', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'X', 'O', 'X', 'X'] ]
    self.assertEqual(self.board.end_of_game(), (True, 'Tie'))
    # test all 21 positions of vertical winners
    rows = range(3)
    columns = range(7)
    for row, column in itertools.product(rows, columns):
      self.board.board = copy.deepcopy(self.empty_board)
      self.board.board[row][column] = 'X'
      self.board.board[row + 1][column] = 'X'
      self.board.board[row + 2][column] = 'X'
      self.board.board[row + 3][column] = 'X'
      self.assertEqual(self.board.end_of_game(), (True, 'X')) 
    # test all 24 positions of horizontal winners
    rows = range(6)
    columns = range(4) 
    for row, column in itertools.product(rows, columns):
      self.board.board = copy.deepcopy(self.empty_board)
      self.board.board[row][column] = 'O'
      self.board.board[row][column + 1] = 'O'
      self.board.board[row][column + 2] = 'O'
      self.board.board[row][column + 3] = 'O'
      self.assertEqual(self.board.end_of_game(), (True, 'O'))
    # test all 12 positions of diagonal down winners
    rows = range(3)
    columns = range(4)
    for row, column in itertools.product(rows, columns):
      self.board.board = copy.deepcopy(self.empty_board)
      self.board.board[row][column] = 'O'
      self.board.board[row + 1][column + 1] = 'O'
      self.board.board[row + 2][column + 2] = 'O'
      self.board.board[row + 3][column + 3] = 'O'
      self.assertEqual(self.board.end_of_game(), (True, 'O'))
    # test all 12 positions of diagonal up winners  
    rows = range(3, 6)
    columns = range(4)
    for row, column in itertools.product(rows, columns):
      self.board.board = copy.deepcopy(self.empty_board)
      self.board.board[row][column] = 'X'
      self.board.board[row - 1][column + 1] = 'X'
      self.board.board[row - 2][column + 2] = 'X'
      self.board.board[row - 3][column + 3] = 'X'
      self.assertEqual(self.board.end_of_game(), (True, 'X'))

class TestMoveDecisionBase(unittest.TestCase):

  def setUp(self):
    self.decision = MoveDecisionBase(Board().get_board())
    self.empty_board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '] ]

  def test_available_moves(self):
    self.decision.get_available_moves()
    self.assertEqual(self.decision.available_moves, [0, 1, 2, 3, 4, 5, 6])
    # check all columns
    for column in range(7):
      board = copy.deepcopy(self.empty_board)
      board[0][column] = 'O'
      board[1][column] = 'X'
      board[2][column] = 'O'
      board[3][column] = 'O'
      board[4][column] = 'X'
      board[5][column] = 'X'
      expected = list(range(7))
      expected.pop(column)
      self.decision = MoveDecisionBase(board)
      self.decision.get_available_moves()
      self.assertEqual(self.decision.available_moves, expected)

class TestMoveDecisionEasy(unittest.TestCase):

  def setUp(self):
    self.decision = MoveDecisionEasy(Board().get_board())
    self.empty_board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '] ]

  def test_move(self):
    # check that the randomly selected column isn't full (for each column)
    for column in range(7):
      board = copy.deepcopy(self.empty_board)
      board[0][column] = 'O'
      board[1][column] = 'X'
      board[2][column] = 'O'
      board[3][column] = 'O'
      board[4][column] = 'X'
      board[5][column] = 'X'
      self.decision = MoveDecisionEasy(board)
      self.assertNotEqual(self.decision.move(), column)          

if __name__ == '__main__':
  unittest.main()