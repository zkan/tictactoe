import os
import random


def print_board(board):
    print "         |         |         "
    print "    %s    |    %s    |    %s    " % (board[0], board[1], board[2])
    print "_________|_________|_________"
    print "         |         |         "
    print "    %s    |    %s    |    %s    " % (board[3], board[4], board[5])
    print "_________|_________|_________"
    print "         |         |         "
    print "    %s    |    %s    |    %s    " % (board[6], board[7], board[8])
    print "         |         |         "


#board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#print_board(board)
#os.system('clear')
