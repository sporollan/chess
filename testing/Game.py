import game
import unittest
from parameterized import parameterized


class Test_game(unittest.TestCase):
    def setUp(self):
        self.g = game.Game()

    @parameterized.expand((
        ('white moves pawn', 1, (6, 0), (5, 0),
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]),
        ('select cancel move', 1, (6, 0), (2, 0),
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]),
    ))
    def test_play_double_input(self, name, turn, spot1, spot2, expected1, expected2):
        self.g.turn = turn
        board = self.g.play(spot1)
        self.assertEqual(board, expected1)
        board = self.g.play(spot2)
        self.assertEqual(board, expected2)

    @parameterized.expand([
        ('white castlign right',
            [[' ', 'R0', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             ['R1', ' ', ' ', ' ', 'K1', ' ', ' ', 'R1']],
             1, ((1, 1), (1, 1)), ((1, 1), (1, 1)),
             ((1, 1), (1, 1)), ((1, 1), (1, 1)),
             ((1, 1), (1, 1)), ((7, 4), (7, 6)),
            [[' ', 'R', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', '*', '*', '*', ' ', ' '],
             ['R', '*', ' ', '*', 'K', '*', '*', 'R']],
            [[' ', 'R', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['R', ' ', ' ', ' ', ' ', 'R', 'K', ' ']]),
        ('white castlign left',
            [[' ', 'R0', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             [' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' '],
             ['R1', ' ', ' ', ' ', 'K1', ' ', ' ', 'R1']],
             1, ((1, 1), (1, 1)), ((1, 1), (1, 1)),
             ((1, 1), (1, 1)), ((1, 1), (1, 1)),
             ((1, 1), (1, 1)), ((7, 4), (7, 1)),
            [[' ', 'R', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', '*', '*', '*', ' ', ' '],
             ['R', '*', ' ', '*', 'K', '*', '*', 'R']],
            [[' ', 'R', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'K', 'R', ' ', ' ', ' ', ' ', 'R']]),
    ])
    def test_castling(self, name, custom_board, turn, move1, move2, move3, move4, move5, move6, expected_movearray, expected):
        self.g.turn = turn
        self.g.board.set_custom_board(custom_board)
        board = self.g.play(move1[0])
        board = self.g.play(move1[1])
        board = self.g.play(move2[0])
        board = self.g.play(move2[1])
        board = self.g.play(move3[0])
        board = self.g.play(move3[1])
        board = self.g.play(move4[0])
        board = self.g.play(move4[1])
        board = self.g.play(move5[0])
        board = self.g.play(move5[1])
        board = self.g.play(move6[0])
        self.assertEqual(board, expected_movearray)
        board = self.g.play(move6[1])
        self.assertEqual(board, expected)


    @parameterized.expand([
        ((6, 0), (5, 0), (0, 1), (2, 2), (7, 0), (6, 0),
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['*', ' ', '*', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', ' ', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', 'N', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', ' ', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', 'N', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', ' ', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', 'N', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['R', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]),
        ((6, 4), (5, 4), (1, 0), (2, 0), (7, 5), (2, 0),
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', '*', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['P*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', '*', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', '*', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', '*', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', '*', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['B', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', ' ', 'N', 'R']]),
        ((1, 0), (7, 1), (1, 0), (7, 6), (5, 5), (1, 6),
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['*', ' ', '*', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'N', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', ' ', 'R']],
            [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             [' ', ' ', ' ', ' ', ' ', ' ', '*', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'N', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', ' ', 'R']])
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
        ('white moves bishop',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', ' ',  ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'B1', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', ' ',  ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
             1, (4, 3),
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P', ' ', ' ',  ' ', 'P', ' ', ' ',],
             [' ', ' ',  '*', ' ',  '*', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'B', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  '*', ' ',  '*', ' ',  ' ', ' ',],
             [' ', 'P', ' ', ' ',  ' ', 'P', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]]
        ),
        ('white moves bishop',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', ' ',  ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'B1', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', ' ',  ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
             1, (4, 3),
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P*', ' ', ' ',  ' ', 'P*', ' ', ' ',],
             [' ', ' ',  '*', ' ',  '*', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'B', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  '*', ' ',  '*', ' ',  ' ', ' ',],
             [' ', 'P*', ' ', ' ',  ' ', 'P*', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]]
        ),
        ('black moves bishop',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', ' ',  ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'B0', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', ' ',  ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
             0, (4, 3),
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P', ' ', ' ',  ' ', 'P', ' ', ' ',],
             [' ', ' ',  '*', ' ',  '*', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'B', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  '*', ' ',  '*', ' ',  ' ', ' ',],
             [' ', 'P', ' ', ' ',  ' ', 'P', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]]
        ),
        ('black moves bishop',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', ' ',  ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'B0', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', ' ',  ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
             0, (4, 3),
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P*', ' ', ' ',  ' ', 'P*', ' ', ' ',],
             [' ', ' ',  '*', ' ',  '*', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'B', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  '*', ' ',  '*', ' ',  ' ', ' ',],
             [' ', 'P*', ' ', ' ',  ' ', 'P*', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]]
        ),
        ('black moves rook',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'P0', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', 'R0', ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'P0', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  ' ', ' ',]],
             0, (4, 3),
            [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ',],
             [' ', 'P', '*', 'R', '*', 'P', ' ', ' ',],
             [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]],
        ),
        ('black moves rook',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'P1', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', 'R0', ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'P1', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  ' ', ' ',]],
             0, (4, 3),
            [[' ', ' ', ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', 'P*', ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', '*',  ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', '*',  ' ', ' ',  ' ', ' ',],
             [' ', 'P*', '*', 'R', '*', 'P*', ' ', ' ',],
             [' ', ' ', ' ', '*',  ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', 'P*', ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', ' ',  ' ', ' ',  ' ', ' ',]],
        ),
        ('white moves rook',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'P1', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', 'R1', ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'P1', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  ' ', ' ',]],
             1, (4, 3),
            [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ',],
             [' ', 'P', '*', 'R', '*', 'P', ' ', ' ',],
             [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]],
        ),
        ('white moves rook',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'P0', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', 'R1', ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', 'P0', ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  ' ', ' ',]],
             1, (4, 3),
            [[' ', ' ', ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', 'P*', ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', '*',  ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', '*',  ' ', ' ',  ' ', ' ',],
             [' ', 'P*', '*', 'R', '*', 'P*', ' ', ' ',],
             [' ', ' ', ' ', '*',  ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', 'P*', ' ', ' ',  ' ', ' ',],
             [' ', ' ', ' ', ' ',  ' ', ' ',  ' ', ' ',]],
        ),
        ('white moves pawn',
            [[' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', 'P0', ' ', 'P1', ' ', ' ', ' ',],
             [' ', ' ', ' ', 'P1', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ',  ' ', ' ', ' ',]],
             1, (6, 3),
            [[' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', 'P*', '*', 'P', ' ', ' ', ' ',],
             [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ',  ' ', ' ', ' ',]],
        ),
        ('black moves pawn',
            [[' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', 'P0', ' ', ' ', ' ', ' ',],
             [' ', ' ', 'P0', ' ', 'P1', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ',  ' ', ' ', ' ',]],
             0, (4, 3),
            [[' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ',],
             [' ', ' ', 'P', '*', 'P*', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ',  ' ', ' ', ' ',]],
        ),
        ('black moves queen',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', 'P1', ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', 'Q0', ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', 'P1', ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
             0, (4, 3),
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P*', ' ', 'P*', ' ', 'P*', ' ', ' ',],
             [' ', ' ',  '*', '*',  '*', ' ',  ' ', ' ',],
             [' ', 'P*', '*', 'Q',  '*', 'P*', ' ', ' ',],
             [' ', ' ',  '*', '*',  '*', ' ',  ' ', ' ',],
             [' ', 'P*', ' ', 'P*', ' ', 'P*', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
        ),
        ('black moves queen',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', 'P0', ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', 'Q0', ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', 'P0', ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
             0, (4, 3),
            [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', 'P', ' ', 'P', ' ', 'P', ' ', ' ',],
             [' ', ' ', '*', '*', '*', ' ', ' ', ' ',],
             [' ', 'P', '*', 'Q', '*', 'P', ' ', ' ',],
             [' ', ' ', '*', '*', '*', ' ', ' ', ' ',],
             [' ', 'P', ' ', 'P', ' ', 'P', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]],
        ),
        ('white moves queen',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', 'P0', ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', 'Q1', ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P0', ' ', 'P0', ' ', 'P0', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
             1, (4, 3),
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P*', ' ', 'P*', ' ', 'P*', ' ', ' ',],
             [' ', ' ',  '*', '*',  '*', ' ',  ' ', ' ',],
             [' ', 'P*', '*', 'Q',  '*', 'P*', ' ', ' ',],
             [' ', ' ',  '*', '*',  '*', ' ',  ' ', ' ',],
             [' ', 'P*', ' ', 'P*', ' ', 'P*', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
        ),
        ('white moves queen',
            [[' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', 'P1', ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', 'Q1', ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',],
             [' ', 'P1', ' ', 'P1', ' ', 'P1', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ', ' ',  ' ', ' ',]],
             1, (4, 3),
            [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
             [' ', 'P', ' ', 'P', ' ', 'P', ' ', ' ',],
             [' ', ' ', '*', '*', '*', ' ', ' ', ' ',],
             [' ', 'P', '*', 'Q', '*', 'P', ' ', ' ',],
             [' ', ' ', '*', '*', '*', ' ', ' ', ' ',],
             [' ', 'P', ' ', 'P', ' ', 'P', ' ', ' ',],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]],
        ),
    ])
    def test_pieces_movearray(self, name, custom_board, turn, spot, expected):
        self.g.board.set_custom_board(custom_board)
        self.g.turn = turn
        self.assertEqual(self.g.play(spot), expected)

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
             1, (4, 3), (4, 4)
        ),
        (
            [[' ', ' ',  ' ', ' ',  'K0', ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', 'R0', ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', ' ',  ' ', ' ',  ' ',  ' ', ' ', ' ',],
             [' ', 'K1', ' ', ' ',  ' ',  ' ', ' ', ' ',]],
             0, (4, 3), (4, 1)
        ),
    ])
    def test_check(self, custom_board, turn, move_start, move_end):
        self.g.board.set_custom_board(custom_board)
        self.g.turn = turn
        self.g.play(move_start)
        self.g.play(move_end)
        self.assertTrue(self.g.check)
        self.assertFalse(self.g.check_mate)

    @parameterized.expand([
        (
            [[' ', ' ',  ' ', ' ', ' ',  ' ',  ' ',  'K0',],
             [' ', ' ',  ' ', ' ', ' ',  'Q1', ' ',  ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  'R1', ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  ' ',  ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  ' ',  ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  ' ',  ' ',],
             [' ', ' ',  ' ', ' ', ' ',  ' ',  ' ',  ' ',],
             [' ', 'K1', ' ', ' ', ' ',  ' ',  ' ',  ' ',]],
             1, (1, 5), (1, 6), False, False
        ),
        (
            [[' ',  ' ',  ' ',  ' ',  'K0', ' ', ' ', ' ',],
             [' ',  ' ',  ' ',  ' ',  ' ',  ' ', ' ', ' ',],
             [' ',  ' ',  ' ',  ' ',  ' ',  ' ', ' ', ' ',],
             [' ',  ' ',  ' ',  ' ',  ' ',  ' ', ' ', ' ',],
             [' ',  'R0', ' ',  ' ',  ' ',  ' ', ' ', ' ',],
             [' ',  ' ',  ' ',  ' ',  ' ',  ' ', ' ', ' ',],
             [' ',  ' ',  'Q0', ' ',  ' ',  ' ', ' ', ' ',],
             ['K1', ' ',  ' ',  ' ',  ' ',  ' ', ' ', ' ',]],
             0, (6, 2), (6, 1), False, False
        ),
    ])
    def test_check_mate(self, custom_board, turn, move_start, move_end, castling_white, castling_black):
        self.g.board.set_custom_board(custom_board)
        self.g.turn = turn
        self.g.board.board[0][self.g.board.get_king(0)].can_castle = castling_black
        self.g.board.board[1][self.g.board.get_king(1)].can_castle = castling_white
        self.g.play(move_start)
        self.g.play(move_end)
        self.assertTrue(self.g.check)
        self.assertTrue(self.g.check_mate)
