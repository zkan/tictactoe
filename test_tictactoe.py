from io import BytesIO as StringIO
from mock import patch
import unittest

import tictactoe


class TicTacToeTest(unittest.TestCase):
    def test_display_board_should_print_board_to_stdout(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            tictactoe.display_board(board)
            expected = '     |     |     \n'
            expected += '  1  |  2  |  3  \n'
            expected += '_____|_____|_____\n'
            expected += '     |     |     \n'
            expected += '  4  |  5  |  6  \n'
            expected += '_____|_____|_____\n'
            expected += '     |     |     \n'
            expected += '  7  |  8  |  9  \n'
            expected += '     |     |     \n'
            self.assertEqual(fake_output.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
