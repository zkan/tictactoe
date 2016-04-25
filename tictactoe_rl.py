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

    def play_game(self, train=True):
        if not train:
            print '\nNew game!'

        self.playerX.start_game()
        self.playerO.start_game()
        while True:
            if self.playerX_turn:
                player, char, other_player = self.playerX, 'X', self.playerO
            else:
                player, char, other_player = self.playerO, 'O', self.playerX

            if player.breed == "human":
                self.display_board()

            move = player.move(self.board)
            self.board[move - 1] = char

            if self.player_wins(char):
                player.reward(1, self.board)
                other_player.reward(-1, self.board)
                if not train:
                    self.display_board()
                    print char + ' wins!'
                break

            if self.board_full():
                player.reward(0.5, self.board)
                other_player.reward(0.5, self.board)
                if not train:
                    self.display_board()
                    print 'Draw!'
                break

            other_player.reward(0, self.board)
            self.playerX_turn = not self.playerX_turn


class Player(object):
    def __init__(self):
        self.breed = 'human'

    def start_game(self):
        pass

    def move(self, board):
        return int(raw_input('Your move? '))

    def available_moves(self, board):
        return [i + 1 for i in range(0, 9) if board[i] == ' ']

    def reward(self, value, board):
        pass


class QLearningPlayer(Player):
    def __init__(self):
        self.breed = 'qlearner'
        self.q = {}
        self.epsilon = 0.2
        self.alpha = 0.1
        self.gamma = 0.9

    def start_game(self):
        self.last_state = (' ',) * 9
        self.last_move = None

    def getQ(self, state, action):
        pass

    def move(self, board):
        pass

    def reward(self, value, board):
        pass

    def learn(self, state, action, reward, result_state):
        pass


p1 = QLearningPlayer()
p2 = QLearningPlayer()

for i in xrange(0, 20000):
    t = TicTacToe(p1, p2)
    t.play_game()

p1.epsilon = 0
p2 = Player()

while True:
    t = TicTacToe(p1, p2)
    t.play_game(train=False)

    for each in p1.q:
        print each, p1.q[each]
