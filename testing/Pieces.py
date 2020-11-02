import pieces
import unittest
from parameterized import parameterized


class Test_pieces(unittest.TestCase):

    @parameterized.expand([
        ('white can move', 1, (6, 2), [(5, 2), (4, 2)]),
        ('black can move', 0, (1, 1), [(2, 1), (3, 1)]),
        ('white cant move', 1, (6, 2), [], {(5, 2): True}),
        ('black cant move', 0, (1, 1), [], {(2, 1): True}),
    ])
    def test_pawn(self, name, side, coord, expected, allied_pieces={}):
        p = pieces.Pawn(side)
        self.assertEqual(
            set(p.get_moves(coord[0], coord[1], allied_pieces)), set(expected))

    @parameterized.expand([
        ('white all moves', 1, (1, 1),
            [(0, 0), (2, 2), (3, 3), (4, 4), (5, 5),
                (6, 6), (7, 7), (0, 2), (2, 0)]),
        ('black all moves', 0, (1, 1),
            [(0, 0), (2, 2), (3, 3), (4, 4), (5, 5),
                (6, 6), (7, 7), (0, 2), (2, 0)]),
        ('white restricted moves corners', 1, (1, 1),
            [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)],
            {(0, 0): True, (7, 7): True, (0, 2): True, (2, 0): True}),
    ])
    def test_bishop(self, name, side, coord, expected, allied_pieces={}):
        p = pieces.Bishop(side)
        self.assertEqual(
            set(p.get_moves(coord[0], coord[1], allied_pieces)), set(expected))

    @parameterized.expand([
        ('white can move', 1, (1, 1),
            [(1, 0),
                (0, 1),
                (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]),
        ('black can move', 0, (1, 1),
            [(1, 0),
                (0, 1),
                (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
    ])
    def test_rook(self, name, side, coord, expected):
        p = pieces.Rook(side)
        self.assertEqual(set(p.get_moves(coord[0], coord[1])), set(expected))

    @parameterized.expand([
        ('white can move', 1, (6, 1), [(4, 0), (4, 2)]),
        ('black can move', 0, (1, 1), [(3, 0), (3, 2)])
    ])
    def test_knight(self, name, side, coord, expected):
        p = pieces.Knight(side)
        self.assertEqual(set(p.get_moves(coord[0], coord[1])), set(expected))

    @parameterized.expand([
        ('white can move', 1, (3, 3),
            [(4, 4), (4, 3), (4, 2),
             (3, 2), (3, 4),
             (2, 2), (2, 3), (2, 4)]),
        ('black can move', 0, (3, 3),
            [(4, 4), (4, 3), (4, 2),
             (3, 2), (3, 4),
             (2, 2), (2, 3), (2, 4)]),
    ])
    def test_king(self, name, side, coord, expected):
        p = pieces.King(side)
        self.assertEqual(set(p.get_moves(coord[0], coord[1])), set(expected))

    @parameterized.expand([
        ('white can move', 1, (1, 1),
            [(0, 0), (2, 2), (3, 3), (4, 4), (5, 5),
                (6, 6), (7, 7), (0, 2), (2, 0), (1, 0),
                (0, 1),
                (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]),
        ('black can move', 0, (1, 1),
            [(0, 0), (2, 2), (3, 3), (4, 4), (5, 5),
                (6, 6), (7, 7), (0, 2), (2, 0), (1, 0),
                (0, 1),
                (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
    ])
    def test_queen(self, name, side, coord, expected):
        p = pieces.Queen(side)
        self.assertEqual(set(p.get_moves(coord[0], coord[1])), set(expected))
