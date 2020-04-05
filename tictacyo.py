# Authors: Taylor Ertrachter, tertrachter2017@my.fit.edu
# Course: CSE 4301, Spring 2020
# Project: Assignment 2, NxN Tic-Tac-Toe

from argparse import (ArgumentParser)

#Create node 'structure' including search functions.
class graph_map:
    #What makes up a node, includes possible moves. 
    def __init__(self, board_size=None, board=None): # Constructor  
        self.board_size = board_size
        self.board = ["-"] * (board_size * board_size)
        self.total_moves = (board_size * board_size)
        self.total_available_moves = (board_size * board_size)
        self.next_city = None
    
    #Print game board, is there a better way to do this? Yes. Am I going to do it? Probably not.
    def print_game_board(self):
        new_line = 1
        for i in range(self.total_moves):
            if(new_line == self.board_size):
                print(self.board[i])
                new_line = 1
            else:
                print(self.board[i], end='')
                new_line += 1

    #Max evaluation value, beep boop
    def computer_move(self):
        new_move = 0

        if(self.total_available_moves == 0):
            print("DRAW!")
            return
        #elif() bruh tf is he going on about fr fr
        else:
            value = 0
            for i in range(self.total_moves):
                if(self.board[i] == '-'):
                    new_move = i
        
        self.board[new_move] = 'X'
        self.total_available_moves -= 1

#'main' function
def tictactoe_homework():

    game_board = graph_map(N_ARGS.N)

    while(game_board.total_available_moves != 0):
        game_board.print_game_board()

        show_me_your_moves = input("Your move, human>>")
        game_board.board[int(show_me_your_moves)] = 'O'
        game_board.total_available_moves -= 1

        game_board.computer_move()

#This calls the 'main'
if __name__ == "__main__":

    #Create 'N' argument to capture size of board at run.
    N_PARSER = ArgumentParser()
    N_PARSER.add_argument("--N", type=int, help="Specifies N, size of board NxN")
    N_ARGS = N_PARSER.parse_args()

    tictactoe_homework()