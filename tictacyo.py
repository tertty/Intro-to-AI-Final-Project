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
        self.depth_check = False

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

    def full_board(self):
        for i in self.board:
            if(i == '-'):
                return False
        return True

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
    def computer_move(self, depth):
        new_move = 0

        if((self.depth_check == True) and (depth > 3)):
            return 1

        if(self.full_board()):
            #print("COMPUTER DRAW!")
            return 0
        elif(self.computer_win()):
            #print("Human wins!")
            #self.print_game_board() Debug
            return -1
        else:
            value = float('-inf')
            for i in range(self.total_moves):
                if(self.board[i] == '-'):
                    self.board[i] = 'X'
                    human_response = self.human_move((depth + 1))
                    self.board[i] = '-'
                
                    if(human_response > value):
                        value = human_response
                        new_move = i

            return new_move
    
    #Min evaluation value, boop beep
    def human_move(self, depth):
        new_move = 0

        if((self.depth_check == True) and (depth > 3)):
            return -1

        if(self.full_board()):
            #print("HUMAN DRAW!")
            return 0
        elif(self.human_win()):
            #print("Computer wins!")
            return 1
        else:
            value = float('inf')
            for i in range(self.total_moves):
                if(self.board[i] == '-'):
                    self.board[i] = 'O'
                    computer_response = self.computer_move((depth + 1))
                    self.board[i] = '-'
                
                    if(computer_response < value):
                        value = computer_response
                        new_move = i
                    
            return new_move

#'main' function
def tictactoe_homework():

    game_board = graph_map(N_ARGS.N)

    if(N_ARGS.N > 3):
        game_board.depth_check = True

    game_board.board[game_board.computer_move(0)] = 'X'
    game_board.total_available_moves -= 1

    while(game_board.total_available_moves > 0):
        print("Moves left:", game_board.total_available_moves)

        game_board.print_game_board()

        #show_me_your_moves = input("Your move, human>>")
        #game_board.board[int(show_me_your_moves)] = 'O'
        
        #Human automated move
        human_move = game_board.human_move(0)
        print("Human move:", human_move)
        game_board.board[human_move] = 'O'
        game_board.total_available_moves -= 1

        #Computer automated move
        computer_move = game_board.computer_move(0)
        print("Computer move:", computer_move)
        game_board.board[computer_move] = 'X'
        game_board.total_available_moves -= 1

    game_board.print_game_board()
    print("Game over!")

#This calls the 'main'
if __name__ == "__main__":

    #Create 'N' argument to capture size of board at run.
    N_PARSER = ArgumentParser()
    N_PARSER.add_argument("--N", type=int, help="Specifies N, size of board NxN")
    N_ARGS = N_PARSER.parse_args()

    tictactoe_homework()