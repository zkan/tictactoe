from io import BytesIO as StringIO
from mock import patch
import unittest

from tictactoe import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def test_display_board_should_print_board_to_stdout(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            game = TicTacToe()
            game.display_board()
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


if __name__ == '__main__':
    unittest.main()
