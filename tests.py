import unittest
import unittest.mock
import sys

from board import Board
from cli import CLI

# class TestIO(unittest.TestCase):

#   def setUp(self):
#     self.cli = CLI()

#   def test_input_difficulty(self):
#     # map each valid input to its expected output
#     valid_data = {}
#     for level in ['Easy', 'Medium', 'Hard']:
#       value = level[0]
#       valid_data[level] = value
#       valid_data[level.upper()] = value
#       valid_data[level.lower()] = value
#       valid_data[level[0]] = value
#       valid_data[level[0].lower()] = value
#     for input_str, return_val in valid_data.items():
#       with unittest.mock.patch('builtins.input', return_value=input_str):
#         self.assertEqual(self.cli.input_difficulty(), return_val)
#     invalid_data = iter(['', 'a', ' ', '\n', 0, 'xyz', '5', '$', '__', 'v'])
#     with unittest.mock.patch('builtins.input', return_value=next(invalid_data)):
#       self.assertRaises(SystemExit, self.cli.input_difficulty)
#   def test_input_move(self):
#     valid_data = ['0', '1', '2', '3', '4', '5', '6']
#     for input_str in valid_data:
#       with unittest.mock.patch('builtins.input', return_value=input_str):
#         self.assertEqual(self.cli.input_move(), int(input_str))
#     invalid_data = iter(['', 'a', ' ', '\n', 'three', 'z', '$', '_', '+', 'wetw4t4'])
#     with unittest.mock.patch('builtins.input', return_value=next(invalid_data)):
#       self.assertRaises(SystemExit, self.cli.input_move)
#   def test_output_board(self):
#     empty_board = [
#       [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#       [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#       [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#       [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#       [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#       [' ', ' ', ' ', ' ', ' ', ' ', ' ']
#     ]
#     self.cli.output_board(empty_board)
#     full_board = [
#       ['O', 'O', 'O', 'X', 'O', 'O', 'X'],
#       ['X', 'X', 'X', 'O', 'X', 'X', 'O'],
#       ['O', 'X', 'O', 'O', 'X', 'X', 'X'],
#       ['O', 'O', 'X', 'O', 'X', 'O', 'O'],
#       ['O', 'X', 'O', 'X', 'O', 'X', 'X'],
#       ['X', 'O', 'X', 'X', 'O', 'X', 'O']
#     ]
#     self.cli.output_board(full_board)
           
class TestBoard(unittest.TestCase):

  def setUp(self):
    self.board = Board()

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

  def test_check_winner(self):
    # pattern these out somehow 

    # no winners
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '] ]
    self.assertEqual(self.board.check_winner(), False)
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', 'X', 'O', ' ', ' ', ' ', ' '],
      [' ', 'O', 'O', 'X', 'O', ' ', ' '],
      [' ', 'X', 'X', 'O', 'X', 'O', ' '],
      [' ', 'O', 'X', 'X', 'O', 'X', ' '] ]
    self.assertEqual(self.board.check_winner(), False)
    self.board.board = [
      ['X', 'O', 'X', 'X', 'O', 'X', 'O'],
      ['X', 'X', 'O', 'O', 'O', 'X', 'X'],
      ['X', 'O', 'X', 'O', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'O', 'X', 'X', 'X'],
      ['X', 'X', 'O', 'X', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'X', 'O', 'X', 'X'] ]
    self.assertEqual(self.board.check_winner(), False)
    # vertical winners
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      ['O', ' ', ' ', ' ', ' ', ' ', ' '],
      ['O', ' ', ' ', ' ', ' ', ' ', ' '],
      ['O', ' ', ' ', 'X', ' ', ' ', ' '],
      ['O', ' ', 'X', 'X', 'X', ' ', ' '] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      ['X', ' ', ' ', ' ', ' ', ' ', ' '],
      ['X', ' ', ' ', ' ', ' ', ' ', ' '],
      ['X', ' ', ' ', ' ', ' ', ' ', ' '],
      ['X', ' ', ' ', ' ', ' ', 'O', ' '],
      ['O', ' ', ' ', 'X', 'X', 'O', ' '],
      ['O', ' ', 'X', 'O', 'O', 'X', 'O'] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', 'X', ' ', ' ', ' '],
      [' ', ' ', ' ', 'X', 'O', ' ', ' '],
      [' ', ' ', 'O', 'X', 'X', ' ', ' '],
      [' ', ' ', 'O', 'X', 'O', ' ', ' '] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      [' ', ' ', ' ', ' ', 'O', ' ', ' '],
      [' ', ' ', ' ', ' ', 'O', ' ', ' '],
      [' ', ' ', ' ', ' ', 'O', ' ', ' '],
      [' ', ' ', ' ', 'X', 'O', ' ', ' '],
      [' ', ' ', 'X', 'X', 'X', ' ', 'X'],
      [' ', ' ', 'O', 'O', 'X', 'O', 'X'] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', 'X'],
      [' ', ' ', ' ', ' ', ' ', ' ', 'X'],
      [' ', ' ', 'O', ' ', ' ', ' ', 'X'],
      [' ', ' ', 'O', 'O', ' ', 'O', 'X'] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', 'O'],
      [' ', ' ', ' ', ' ', ' ', ' ', 'O'],
      [' ', ' ', ' ', ' ', ' ', ' ', 'O'],
      [' ', ' ', ' ', ' ', ' ', ' ', 'O'],
      [' ', ' ', 'X', ' ', ' ', ' ', 'X'],
      [' ', 'O', 'X', 'X', 'O', 'X', 'X'] ]
    self.assertEqual(self.board.check_winner(), True)
    # horizontal winner
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', 'O', 'O', ' ', ' '],
      [' ', 'X', 'X', 'X', 'X', 'O', ' '] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', 'X', 'X', ' ', ' '],
      ['O', 'O', 'O', 'O', 'X', 'X', ' '] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', 'X', 'X', ' ', ' '],
      [' ', 'X', 'X', 'O', 'O', 'O', 'O'] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      ['X', 'X', 'X', 'X', 'O', 'X', 'O'],
      ['X', 'X', 'O', 'O', 'O', 'X', 'X'],
      ['X', 'O', 'O', 'O', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'O', 'X', 'X', 'X'],
      ['X', 'X', 'O', 'X', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'X', 'O', 'X', 'X'] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      ['X', 'X', 'X', 'O', 'O', 'O', 'O'],
      ['X', 'X', 'O', 'X', 'O', 'X', 'X'],
      ['X', 'O', 'X', 'O', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'O', 'X', 'X', 'X'],
      ['X', 'X', 'O', 'X', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'X', 'O', 'X', 'X'] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      ['X', 'O', 'X', 'X', 'X', 'X', 'O'],
      ['X', 'X', 'O', 'X', 'O', 'X', 'X'],
      ['X', 'O', 'X', 'O', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'O', 'X', 'X', 'X'],
      ['X', 'X', 'O', 'X', 'X', 'O', 'O'],
      ['O', 'O', 'X', 'X', 'O', 'X', 'X'] ]
    self.assertEqual(self.board.check_winner(), True)
    # diagonal winners
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', 'O', ' ', ' ', ' ', ' ', ' '],
      [' ', 'X', 'O', ' ', ' ', ' ', ' '],
      [' ', 'X', 'X', 'O', 'X', ' ', ' '],
      [' ', 'O', 'X', 'X', 'O', 'O', ' '] ]
    self.assertEqual(self.board.check_winner(), True)
    self.board.board = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', 'O'],
      [' ', ' ', ' ', ' ', ' ', 'O', 'X'],
      [' ', ' ', ' ', 'X', 'O', 'O', 'O'],
      [' ', ' ', ' ', 'O', 'X', 'X', 'X'],
      [' ', ' ', ' ', 'X', 'X', 'O', 'X'] ]
    self.assertEqual(self.board.check_winner(), True)

if __name__ == '__main__':
  unittest.main()