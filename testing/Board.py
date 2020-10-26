import board
import moves
import unittest


class Test_board(unittest.TestCase):
    def setUp(self):
        self.b = board.Board()

    def test_init_board(self):
        expected = [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
                    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                    ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']]
        self.assertEqual(self.b.get_board(), expected)

    def test_isPiece(self):
        self.assertTrue(self.b.isPiece(6, 0, 1))

    def test_move(self):
        move = moves.Move(1, (6, 0), (5, 0))
        self.b.move(move)
        expected = [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
                    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                    ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']]
        self.assertEqual(self.b.get_board(), expected)

    def test_set_custom_board(self):
        cb =       [[' ',  ' ', ' ',   'K0', ' ',  ' ', ' ',  ' '],
                    [' ',  ' ', ' ',   ' ',  ' ',  ' ', 'P0', 'P0'],
                    [' ',  'R0', 'R1', ' ',  ' ',  ' ', ' ',  ' '],
                    [' ',  'B1', 'B0', ' ',  ' ',  ' ', ' ',  ' '],
                    [' ',  ' ',  ' ',  ' ',  ' ',  ' ', ' ',  ' '],
                    [' ',  ' ',  ' ',  ' ',  ' ',  ' ', 'P1', 'P1'],
                    [' ',  ' ',  ' ',  ' ',  ' ',  ' ', ' ',  ' '],
                    [' ',  ' ',  ' ',  ' ',  'K1', ' ', ' ',  ' ']]
        self.b.set_custom_board(cb)
        expected = [[' ', ' ', ' ', 'K', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', 'P', 'P'],
                    [' ', 'R', 'R', ' ', ' ', ' ', ' ', ' '],
                    [' ', 'B', 'B', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', 'P', 'P'],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', 'K', ' ', ' ', ' ']]
        self.assertEqual(self.b.get_board(), expected)
