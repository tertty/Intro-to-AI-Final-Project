# Authors: Taylor Ertrachter, tertrachter2017@my.fit.edu
# Nicholas Tolentino, ntolentino2017@my.fit.edu
# Course: CSE 4301, Spring 2020
# Project: Assignment 2, NxN Tic-Tac-Toe

from argparse import (ArgumentParser)

#Create node 'structure' including search functions.
class graph_map:
    #What makes up a node, includes possible moves. 
    def __init__(self, board_size=None, board=None): # Constructor  
        self.board_size = board_size
        self.board = ['-'] * (board_size * board_size)
        self.total_moves = (board_size * board_size)
        self.total_available_moves = (board_size * board_size)
        self.depth_check = False

    def show_hint(self):
        new_line = 1
        for i in range(self.total_moves):
            if(new_line == self.board_size):
                print(i, ' ')
                new_line = 1
            else:
                print(i, ' ', end='')
                new_line += 1
        
    def check_for_win(self):
        if(self.computer_win()):
            print("Computer wins, game over!")
            return True
        if(self.human_win()):
            print("Human wins, game over!")
            return True
        return False

    #Checks to see in the Computer moves equal to a win (3 in a row)
    def computer_win(self):

        #Vertical checks
        vertical_answer = False

        for k in range(0,self.total_moves,self.board_size):
            x_check = 0
            for j in range(self.board_size):
                if(self.board[k+j] == 'X'):
                    x_check += 1
            if(x_check == self.board_size):
                vertical_answer = True
            x_check = 0

        #Horizontal checks
        horizontal_answer = False

        for i in range(self.board_size):
            x_check = 0
            for j in range(0,self.total_moves,self.board_size):
                if(self.board[i+j] == 'X'):
                    x_check += 1
            if(x_check == self.board_size):
                horizontal_answer = True
            x_check = 0

        #Diagnal right checks
        diagnal_right_answer = False

        x_check = 0

        for i in range(0,self.total_moves, self.board_size+1):
            if(self.board[i] == 'X'):
                x_check += 1

        if(x_check == self.board_size):
            diagnal_right_answer = True

        #Diagnal left checks
        diagnal_left_answer = False

        x_check = 0

        for i in range(self.board_size-1,self.total_moves-(self.board_size-1), self.board_size-1):
            if(self.board[i] == 'X'):
                x_check += 1

        if(x_check == self.board_size):
            diagnal_left_answer = True

        return (vertical_answer or horizontal_answer or diagnal_right_answer or diagnal_left_answer)
        
    #Checks to see in the Human moves equal to a win (3 in a row)
    def human_win(self):

        #Vertical checks
        vertical_answer = False

        for k in range(0,self.total_moves,self.board_size):
            o_check = 0
            for j in range(self.board_size):
                if(self.board[k+j] == 'O'):
                    o_check += 1
            if(o_check == self.board_size):
                vertical_answer = True
            o_check = 0

        #Horizontal checks
        horizontal_answer = False

        for i in range(self.board_size):
            o_check = 0
            for j in range(0,self.total_moves,self.board_size):
                if(self.board[i+j] == 'O'):
                    o_check += 1
            if(o_check == self.board_size):
                horizontal_answer = True
            o_check = 0

        #Diagnal right checks
        diagnal_right_answer = False

        o_check = 0

        for i in range(0,self.total_moves, self.board_size+1):
            if(self.board[i] == 'O'):
                o_check += 1

        if(o_check == self.board_size):
            diagnal_right_answer = True

        #Diagnal left checks
        diagnal_left_answer = False

        o_check = 0

        for i in range(self.board_size-1,self.total_moves-(self.board_size-1), self.board_size-1):
            if(self.board[i] == 'O'):
                o_check += 1

        if(o_check == self.board_size):
            diagnal_left_answer = True
        
        return (vertical_answer or horizontal_answer or diagnal_right_answer or diagnal_left_answer)

    #Checks to see if the board is full and if it is then end the game
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
    def computer_move(self, depth, alpha, beta):
        new_move = 0

        if((self.depth_check == True) and (depth > 3)):
            return -1

        if(self.full_board()):
            #print("COMPUTER DRAW!")
            return 0
        elif(self.computer_win()):
            #print("Computer wins!")
            #self.print_game_board()
            return 1
        else:
            value = float('-inf')
            for i in range(self.total_moves):
                if(self.board[i] == '-'):
                    self.board[i] = 'X'
                    human_response = self.human_move((depth + 1), alpha, beta)
                    self.board[i] = '-'
                
                    if(human_response > value):
                        value = human_response
                        new_move = i

                    alpha = max(alpha, value)

                    if beta <= alpha:
                        break

            return new_move
    
    #Min evaluation value, boop beep
    def human_move(self, depth, alpha, beta):
        new_move = 0

        if((self.depth_check == True) and (depth > 3)):
            return 1

        if(self.full_board()):
            #print("HUMAN DRAW!")
            return 0
        elif(self.human_win()):
            #print("Human wins!")
            #self.print_game_board()
            return -1
        else:
            value = float('inf')
            for i in range(self.total_moves):
                if(self.board[i] == '-'):
                    self.board[i] = 'O'
                    computer_response = self.computer_move((depth + 1), alpha, beta)
                    self.board[i] = '-'
                
                    if(computer_response < value):
                        value = computer_response
                        new_move = i
                    
                    beta = min(beta, value)

                    if beta <= alpha:
                        break
                    
            return new_move

    def next_move(self, is_comp):

        best_val = float('-inf')
        best_move = 0

        for i in range(self.total_moves):
            if(self.board[i] == '-'):

                if(is_comp):
                    self.board[i] = 'X'
                    response = self.computer_move(0, float('-inf'), float('inf'))
                else:
                    self.board[i] = 'O'
                    response = self.human_move(0, float('-inf'), float('inf'))
                self.board[i] = '-'
            
                if(response > best_val):
                    best_val = response
                    best_move = i
                
        return best_move


#'main' function
def tictactoe_homework():

    game_board = graph_map(N_ARGS.N)
    
    #Checks to see if you are playing on bigger than a 3x3 board
    if(N_ARGS.N > 5):
        game_board.depth_check = True

    #
    game_board.board[game_board.next_move(True)] = 'X'
    game_board.total_available_moves -= 1

    print("Current board:")
    game_board.print_game_board()

    while(game_board.total_available_moves > 0):
        print("Moves left:", game_board.total_available_moves)

        if (N_ARGS.M == "H"):
            game_board.show_hint()
            show_me_your_moves = input("Your move, human>>")
            game_board.board[int(show_me_your_moves)] = 'O'
        else:    
            #Human automated move
            human_move = game_board.next_move(False)
            print("Human move:", human_move)
            game_board.board[human_move] = 'O'
        game_board.total_available_moves -= 1
        if(game_board.check_for_win()):
            print("Final board:")
            game_board.print_game_board()
            return

        print("Current board:")
        game_board.print_game_board() 

        #Computer automated move
        computer_move = game_board.next_move(True)
        print("Computer move:", computer_move)
        game_board.board[computer_move] = 'X'
        game_board.total_available_moves -= 1
        if(game_board.check_for_win()):
            print("Final board:")
            game_board.print_game_board()
            return 

        print("Current board:")
        game_board.print_game_board() 

    print("Final board:")
    game_board.print_game_board()
    if(not game_board.check_for_win()): 
        print("Draw, game over!")

#This calls the 'main'
if __name__ == "__main__":

    #Create 'N' argument to capture size of board at run.
    N_PARSER = ArgumentParser()
    N_PARSER.add_argument("--N", type=int, help="Specifies N, size of board NxN")
    N_PARSER.add_argument("--M", type=str, help="Specifies whether the game should be (C)omputer vs Computer or (H)uman vs Computer")
    N_ARGS = N_PARSER.parse_args()

    tictactoe_homework()