from io import BytesIO as StringIO
from mock import patch
import unittest

from tictactoe import (
    MinimaxPlayer,
    Player,
    TicTacToe,
)


class TicTacToeTest(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_display_board_should_print_board_to_stdout(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.game.display_board()
            expected = '     |     |     \n'
            expected += '     |     |     \n'
            expected += '_____|_____|_____\n'
            expected += '     |     |     \n'
            expected += '     |     |     \n'
            expected += '_____|_____|_____\n'
            expected += '     |     |     \n'
            expected += '     |     |     \n'
            expected += '     |     |     \n'
            self.assertEqual(fake_output.getvalue(), expected)

    def test_board_full_should_return_true_if_no_space_left(self):
        self.game.board = ['X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X']
        result = self.game.board_full()
        self.assertTrue(result)

    def test_board_full_should_return_false_if_some_space_left(self):
        self.game.board = ['X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', ' ']
        result = self.game.board_full()
        self.assertFalse(result)

    def test_player_x_wins_should_return_true(self):
        possible_wins = [
            ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X'],
            ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' '],
            [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' '],
            [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X'],
            ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X'],
            [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' '],
        ]
        for each in possible_wins:
            self.game.board = each
            result = self.game.player_wins('X')
            self.assertTrue(result)

    def test_player_x_not_yet_win_should_return_false(self):
        self.game.board = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        result = self.game.player_wins('X')
        self.assertFalse(result)

    def test_play_minimax_game_should_do_nothing(self):
        self.assertIsNone(self.game.play_minimax_game())

    def test_play_rl_game_should_do_nothing(self):
        self.assertIsNone(self.game.play_rl_game())


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.p = Player()

    def test_breed_should_be_human(self):
        expected = 'human'
        self.assertEqual(self.p.breed, expected)

    def test_start_game_should_do_nothing(self):
        self.assertIsNone(self.p.start_game())

    @patch('tictactoe.raw_input')
    def test_move_should_call_raw_input_with_text(self, mock):
        self.p.move()
        mock.assert_called_once_with('Your move? ')

    @patch('tictactoe.raw_input')
    def test_move_should_return_integer(self, mock):
        mock.return_value = '1'
        result = self.p.move()
        self.assertEqual(result, 1)

    def test_available_moves_should_return_list_of_available_moves(self):
        board = ['X', 'X', 'O', 'X', ' ', 'O', 'O', ' ', ' ']
        result = self.p.available_moves(board)
        expected = [5, 8, 9]
        self.assertEqual(result, expected)


class MinimaxPlayerTest(unittest.TestCase):
    def setUp(self):
        self.p = MinimaxPlayer()
        self.p.start_game()

    def test_breed_should_be_minimax(self):
        expected = 'minimax'
        self.assertEqual(self.p.breed, expected)

    def test_start_game_should_set_x_to_itself_and_o_to_enemy(self):
        self.assertEqual(self.p.me, 'X')
        self.assertEqual(self.p.enemy, 'O')

    def test_terminal_state_should_return_true_and_1_if_x_wins(self):
        board = ['X', 'X', 'X', ' ', ' ', 'O', 'O', ' ', ' ']
        result = self.p.in_terminal_state(board)
        self.assertEqual(result, (True, 1))

    def test_terminal_state_should_return_true_and_minus_1_if_o_wins(self):
        board = ['O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O']
        result = self.p.in_terminal_state(board)
        self.assertEqual(result, (True, -1))

    def test_terminal_state_should_return_true_and_0_if_board_is_full(self):
        board = ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O']
        result = self.p.in_terminal_state(board)
        self.assertEqual(result, (True, 0))

    def test_max_value_should_return_1_if_x_wins(self):
        board = ['X', 'X', 'X', ' ', ' ', 'O', 'O', ' ', ' ']
        result = self.p.max_value(board)
        self.assertEqual(result, 1)

    def test_max_value_should_return_minus_1_if_o_wins(self):
        board = ['O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O']
        result = self.p.max_value(board)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
