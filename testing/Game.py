import game
import unittest
from parameterized import parameterized


class Test_game(unittest.TestCase):
    def setUp(self):
        self.g = game.Game()

    @parameterized.expand([
        ((6, 0), (5, 0),
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']]),
        ((6, 0), (2, 0),
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']]),
    ])
    def test_play_double_input(self, spot1, spot2, expected1, expected2):
        board = self.g.play(spot1)
        self.assertEqual(board, expected1)
        board = self.g.play(spot2)
        self.assertEqual(board, expected2)

    @parameterized.expand([
        ((6, 0), (5, 0), (0, 1), (2, 2), (7, 0), (6, 0),
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['*', ' ', '*', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', ' ', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', 'k', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', ' ', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', 'k', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', ' ', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', 'k', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['R', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']]),
        ((6, 4), (5, 4), (1, 0), (2, 0), (7, 5), (2, 0),
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', '*', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['P*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', '*', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', '*', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', '*', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', '*', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['B', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', ' ', 'k', 'R']]),
        ((1, 0), (7, 1), (1, 0), (7, 6), (5, 5), (1, 6),
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', ' ', '*', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'k', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', ' ', 'R']],
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', '*', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'k', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', ' ', 'R']])
    ])
    def test_play_inputx6(self, spot1, spot2, spot3, spot4, spot5, spot6,
                          expected1, expected2, expected3,
                          expected4, expected5, expected6):
        board = self.g.play(spot1)
        self.assertEqual(board, expected1)
        board = self.g.play(spot2)
        self.assertEqual(board, expected2)
        board = self.g.play(spot3)
        self.assertEqual(board, expected3)
        board = self.g.play(spot4)
        self.assertEqual(board, expected4)
        board = self.g.play(spot5)
        self.assertEqual(board, expected5)
        board = self.g.play(spot6)
        self.assertEqual(board, expected6)
        self.assertFalse(self.g.check)

    @parameterized.expand([
        (
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', '*', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'k', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', ' ', 'R']],
             (),
            [['R', 'k', 'B', 'Q', 'K', 'B', 'k', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', '*', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'k', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'k', 'B', 'Q', 'K', 'B', ' ', 'R']]
        )
    ])
    def test_pieces_movearray(self, board, spot, expected):
        pass
        # self.g.board = board
        # self.assertEqual(self.g.play(spot), expected)

    @parameterized.expand([
        (
            [[' ', ' ',  ' ', ' ',  'K0', ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', 'R1', ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', 'K1', ' ', ' ',  ' ',  ' ', ' ', ' ',]],
             (4, 3), (4, 4)),
    ])
    def test_check(self, custom_board, move_start, move_end):
        self.g.board.set_custom_board(custom_board)
        self.g.play(move_start)
        self.g.play(move_end)
        self.assertTrue(self.g.check)
