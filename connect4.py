import sys

from cli import CLI
from board import Board 
from move_decision import MoveDecisionEasy, MoveDecisionMedium, MoveDecisionHard

def main():
  cli = CLI()
  board = Board()
  
  cli.begin()
  difficulty = cli.input_difficulty()
  if difficulty == 'E':
    computer_move = MoveDecisionEasy
  elif difficulty == 'M':
    computer_move = MoveDecisionMedium
  elif difficulty == 'H':
    computer_move = MoveDecisionHard
  else:
    print("Unexpected error, exiting")
    sys.exit()      

  human_is_next = False
  human_is_player_1 = False
  if board.human_goes_first():
    cli.human_is('player 1')
    human_is_next = True
    human_is_player_1 = True
  else:
    cli.human_is('player 2')  

  while True:
    cli.output_board(board.get_board())
    end = board.end_of_game()
    if end[0]:
      if end[1] == 'Tie':
        cli.end_tie()
        break
      elif end[1] == 'X':
        cli.end_winner('Player 1')
        break
      elif end[1] == 'O':
        cli.end_winner('Player 2')
        break
    if human_is_next:
      board.move(cli.input_move(), human_is_player_1)
      human_is_next = False
    else:
      cli.computers_move()
      board.move(computer_move(board.get_board()).move(), (not human_is_player_1))
      human_is_next = True
    
  cli.thanks()  


if __name__ == '__main__':
  main()  