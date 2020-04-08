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

    def computer_win(self):
        new_line = 1
        diag_list = []
        for i in range(self.total_moves):
            if(new_line == self.board_size):
                diag_list.append(self.board[i])

                ex = 0
                dash = 0

                for a in diag_list:
                    if(a == 'X'):
                        ex += 1
                    if(a == '-'):
                        dash += 1

                if((ex == self.board_size-1) and (dash == 1)):
                    return True
                else:
                    new_line = 1
                    diag_list = []
            else:
                diag_list.append(self.board[i])
                new_line += 1
        return False

    def human_win(self):
        new_line = 1
        diag_list = []
        for i in range(self.total_moves):
            if(new_line == self.board_size):
                diag_list.append(self.board[i])

                oh = 0
                dash = 0

                for a in diag_list:
                    if(a == 'O'):
                        oh += 1
                    if(a == '-'):
                        dash += 1

                if((oh == self.board_size-1) and (dash == 1)):
                    return True
                else:
                    new_line = 1
                    diag_list = []
            else:
                diag_list.append(self.board[i])
                new_line += 1
        return False

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
            value = 0
            print("DRAW!")
            return value
        elif(self.computer_win()):
            print("Computer wins!")
            #self.print_game_board() Debug
            return True
        else:
            value = -1
            for i in range(self.total_moves):
                if(self.board[i] == '-'):
                    self.board[i] = 'X'
                    human_response = self.human_move()
                    self.board[i] = '-'
                
                    if(human_response > value):
                        value = human_response
                        new_move = i
                        self.board[new_move] = 'X'
                    
        #self.board[new_move] = 'X'
        #self.total_available_moves -= 1
        return value
    
    #Min evaluation value, boop beep
    def human_move(self):
        new_move = 0

        if(self.total_available_moves == 0):
            value = 0
            print("DRAW!")
            return value
        elif(self.human_win()):
            print("Human wins!")
            return True
        else:
            value = 1
            for i in range(self.total_moves):
                if(self.board[i] == '-'):
                    self.board[i] = 'O'
                    computer_response = self.computer_move()
                    self.board[i] = '-'
                
                    if(computer_response < value):
                        value = computer_response
                        new_move = i
                    
        #self.board[new_move] = 'O'
        #self.total_available_moves -= 1
        return value

#'main' function
def tictactoe_homework():

    game_board = graph_map(N_ARGS.N)

    while(game_board.total_available_moves != 0):
        game_board.computer_move()
        game_board.total_available_moves -= 1

        game_board.print_game_board()

        show_me_your_moves = input("Your move, human>>")
        game_board.board[int(show_me_your_moves)] = 'O'
        game_board.total_available_moves -= 1

#This calls the 'main'
if __name__ == "__main__":

    #Create 'N' argument to capture size of board at run.
    N_PARSER = ArgumentParser()
    N_PARSER.add_argument("--N", type=int, help="Specifies N, size of board NxN")
    N_ARGS = N_PARSER.parse_args()

    tictactoe_homework()