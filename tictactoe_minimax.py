import random


class TicTacToe:
    def __init__(self, playerX, playerO):
        self.board = [' '] * 9
        self.playerX, self.playerO = playerX, playerO
        self.playerX_turn = True

    def display_board(self):
        print '     |     |     '
        print '  %s  |  %s  |  %s  ' % (self.board[0],
                                        self.board[1],
                                        self.board[2])
        print '_____|_____|_____'
        print '     |     |     '
        print '  %s  |  %s  |  %s  ' % (self.board[3],
                                        self.board[4],
                                        self.board[5])
        print '_____|_____|_____'
        print '     |     |     '
        print '  %s  |  %s  |  %s  ' % (self.board[6],
                                        self.board[7],
                                        self.board[8])
        print '     |     |     '

    def board_full(self):
        return not any([space == ' ' for space in self.board])

    def player_wins(self, char):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if char == self.board[a] == self.board[b] == self.board[c]:
                return True

        return False

    def play_game(self):
        print '\nNew game!'

        while True:
            if self.playerX_turn:
                player, char, other_player = self.playerX, 'X', self.playerO
            else:
                player, char, other_player = self.playerO, 'O', self.playerX

            if player.breed == 'human':
                self.display_board()

            move = player.move(self.board)
            self.board[move - 1] = char

            if self.player_wins(char):
                self.display_board()
                print char + ' wins!'
                break

            if self.board_full():
                self.display_board()
                print 'Draw!'
                break

            self.playerX_turn = not self.playerX_turn


class Player(object):
    def __init__(self):
        self.breed = 'human'

    def move(self, board):
        return int(raw_input('Your move? '))

    def available_moves(self, board):
        return [i + 1 for i in range(0, 9) if board[i] == ' ']


class MinimaxPlayer(Player):
    def __init__(self):
        self.breed = 'minimax'

    def move(self, board):
        pass

    def terminal_test(self, board):
        pass

    def max_value(self, board):
        pass

    def min_value(self, board):
        pass


p1 = MinimaxPlayer()
p2 = Player()

while True:
    t = TicTacToe(p1, p2)
    t.play_game()
