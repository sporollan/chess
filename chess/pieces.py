

class Piece():
    def __init__(self, white):
        self.white = white

    def verify_same_team(self, newcoord, allied_pieces):
        if newcoord[0] > 7 or newcoord[0] < 0:
            return []
        if newcoord[1] > 7 or newcoord[1] < 0:
            return []
        try:
            allied_pieces[newcoord]
        except KeyError:
            return [newcoord]
        else:
            return []

    def verify_op_team(self, newcoord, op_pieces):
        try:
            op_pieces[newcoord]
        except KeyError:
            return []
        else:
            return [newcoord]


class Sliding_Piece(Piece):
    def __init__(self, white):
        super().__init__(white)

    def slide(self, moves, newcoord, allied_pieces, op_pieces):
        newmove = self.verify_same_team(newcoord, allied_pieces)
        newmove1 = self.verify_op_team(newcoord, op_pieces)
        if not newmove:
            return False
        elif newmove1:
            moves += newmove
            return False
        elif not newmove1:
            moves += newmove
        else:
            moves += newmove
            return False
        return True


class Hor_Vert_Slider(Sliding_Piece):
    def __init__(self, white):
        super().__init__(white)

    def slide_rook(self, row, col, allied_pieces, op_pieces):
        moves = []
        up, right, down, left = True, True, True, True
        for n in range(1, 8):
            if up:
                newcoord = (row - n, col)
                up = self.slide(moves, newcoord, allied_pieces, op_pieces)
            if right:
                newcoord = (row, col + n)
                right = self.slide(moves, newcoord, allied_pieces, op_pieces)
            if down:
                newcoord = (row + n, col)
                down = self.slide(moves, newcoord, allied_pieces, op_pieces)
            if left:
                newcoord = (row, col - n)
                left = self.slide(moves, newcoord, allied_pieces, op_pieces)
        return moves


class Diagonal_Slider(Sliding_Piece):
    def __init__(self, white):
        super().__init__(white)

    def slide_diagonal(self, row, col, allied_pieces, op_pieces):
        moves = []
        upright, downright, upleft, downleft = True, True, True, True
        for n in range(1, 8):
            if downright:
                newcoord = (row + n, col + n)
                downright = self.slide(moves, newcoord, allied_pieces, op_pieces)
            if downleft:
                newcoord = (row + n, col - n)
                downleft = self.slide(moves, newcoord, allied_pieces, op_pieces)
            if upleft:
                newcoord = (row - n, col - n)
                upleft = self.slide(moves, newcoord, allied_pieces, op_pieces)
            if upright:
                newcoord = (row - n, col + n)
                upright = self.slide(moves, newcoord, allied_pieces, op_pieces)
        return moves


class Castling_Piece(Piece):
    def __init__(self, white):
        super().__init__(white)
        self.can_castle = True
        self.castling = False

    def castle_right(self, row, col, allied_pieces, op_pieces):
        for n in range(1, 3):
            try:
                allied_pieces[(row, col+n)]
                return []
            except KeyError:
                try:
                    op_pieces[(row, col+n)]
                    return []
                except KeyError:
                    if n == 2:
                        try:
                            if allied_pieces[(row, 7)].can_castle:
                                return [(row, col+n)]
                        except KeyError:
                            return []
        return []

    def castle_left(self, row, col, allied_pieces, op_pieces):
        for n in range(1, 4):
            try:
                allied_pieces[(row, col-n)]
                return []
            except KeyError:
                try:
                    op_pieces[(row, col-n)]
                    return []
                except KeyError:
                    if n == 3:
                        try:
                            if allied_pieces[(row, 0)].can_castle:
                                return [(row, col-n)]
                        except KeyError:
                            return []
        return []


class Pawn(Piece):
    def __init__(self, white):
        super().__init__(white)
        self.move_range = 3

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        if self.white:
            return self.__get_white_moves(row, col, allied_pieces, op_pieces)
        else:
            return self.__get_black_moves(row, col, allied_pieces, op_pieces)

    def __get_white_moves(self, row, col, allied_pieces, op_pieces):
        moves = []
        for n in range(1, self.move_range):
            newcoord = (row-n, col)
            if self.verify_same_team(newcoord, allied_pieces) and not self.verify_op_team(newcoord, op_pieces):
                moves.append(newcoord)
            else:
                break
        for n in range(-1, 2, 2):
            moves += self.verify_op_team((row-1, col+n), op_pieces)
        return moves

    def __get_black_moves(self, row, col, allied_pieces, op_pieces):
        moves = []
        for n in range(1, self.move_range):
            newcoord = (row+n, col)
            if self.verify_same_team(newcoord, allied_pieces) and not self.verify_op_team(newcoord, op_pieces):
                moves.append(newcoord)
            else:
                break
        for n in range(-1, 2, 2):
            moves += self.verify_op_team((row+1, col+n), op_pieces)
        return moves

    def get_name(self):
        return 'P'


class Knight(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        if self.white:
            return self.__get_white_moves(row, col, allied_pieces)
        else:
            return self.__get_black_moves(row, col, allied_pieces)

    def __get_white_moves(self, row, col, allied_pieces):
        moves = []
        for n in range(-1, 2, 2):
            newcoord = (row - 2, col + n)
            moves += self.verify_same_team(newcoord, allied_pieces)
        return moves

    def __get_black_moves(self, row, col, allied_pieces):
        return [(row + 2, col + 1), (row + 2, col - 1)]

    def get_name(self):
        return 'N'


class Rook(Hor_Vert_Slider, Castling_Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        return self.slide_rook(row, col, allied_pieces, op_pieces)

    def get_name(self):
        return 'R'


class Bishop(Diagonal_Slider):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        return self.slide_diagonal(row, col, allied_pieces, op_pieces)

    def get_name(self):
        return 'B'


class Queen(Hor_Vert_Slider, Diagonal_Slider):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        moves = []
        moves += self.slide_diagonal(row, col, allied_pieces, op_pieces)
        moves += self.slide_rook(row, col, allied_pieces, op_pieces)
        return moves

    def get_name(self):
        return 'Q'


class King(Castling_Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        moves = []
        for n in range(-1, 2, 2):
            moves += self.verify_same_team((row, col+n), allied_pieces)
            for c in range(-1, 2):
                moves += self.verify_same_team((row + n, col + c), allied_pieces)
        if self.can_castle:
            moves += self.castle_right(row, col, allied_pieces, op_pieces)
            moves += self.castle_left(row, col, allied_pieces, op_pieces)
        return moves

    def get_name(self):
        return 'K'
