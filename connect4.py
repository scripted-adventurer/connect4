from cli import CLI
from board import Board 

def main():
  cli = CLI()
  board = Board()
  
  cli.begin()
  difficulty = cli.input_difficulty()
  print("Success")


if __name__ == '__main__':
  main()  