class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9

    def display_board(self):
        print "     |     |     "
        print "  %s  |  %s  |  %s  " % (self.board[0],
                                        self.board[1],
                                        self.board[2])
        print "_____|_____|_____"
        print "     |     |     "
        print "  %s  |  %s  |  %s  " % (self.board[3],
                                        self.board[4],
                                        self.board[5])
        print "_____|_____|_____"
        print "     |     |     "
        print "  %s  |  %s  |  %s  " % (self.board[6],
                                        self.board[7],
                                        self.board[8])
        print "     |     |     "
