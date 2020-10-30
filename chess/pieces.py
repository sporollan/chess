

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

class Pawn(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        if self.white:
            return self.__get_white_moves(row, col, allied_pieces, op_pieces)
        else:
            return self.__get_black_moves(row, col, allied_pieces, op_pieces)

    def __get_white_moves(self, row, col, allied_pieces, op_pieces):
        moves = []
        moves += self.verify_same_team((row - 1, col), allied_pieces)
        for n in range(-1, 2, 2):
            moves += self.verify_op_team((row-1, col+n), op_pieces)
        return moves

    def __get_black_moves(self, row, col, allied_pieces, op_pieces):
        moves = []
        moves += self.verify_same_team((row + 1, col), allied_pieces)
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


class Rook(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        moves = []
        sliding = [True, True, True, True]
        for n in range(1, 8):
            if row + n <= 7:
                if sliding[0]:
                    newcoord = (row + n, col)
                    newmove = self.verify_same_team(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        sliding[0] = False
            if row - n >= 0:
                if sliding[1]:
                    newcoord = (row - n, col)
                    newmove = self.verify_same_team(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        sliding[1] = False
            if col + n <= 7:
                if sliding[2]:
                    newcoord = (row, col + n)
                    newmove = self.verify_same_team(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        sliding[2] = False
            if col - n >= 0:
                if sliding[3]:
                    newcoord = (row, col - n)
                    newmove = self.verify_same_team(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        sliding[3] = False
        return moves

    def get_name(self):
        return 'R'


class Bishop(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
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

    def get_name(self):
        return 'B'


class Queen(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        moves = []
        for n in range(1, 8):
            colTopFlag = col + n <= 7
            colBotFlag = col - n >= 0
            if row + n <= 7:
                if colTopFlag:
                    moves.append((row + n, col + n))
                if colBotFlag:
                    moves.append((row + n, col - n))
            if row - n >= 0:
                if colBotFlag:
                    moves.append((row - n, col - n))
                if colTopFlag:
                    moves.append((row - n, col + n))
        for n in range(1, 8):
            if row + n <= 7:
                moves.append((row + n, col))
            if row - n >= 0:
                moves.append((row - n, col))
            if col + n <= 7:
                moves.append((row, col + n))
            if col - n >= 0:
                moves.append((row, col - n))
        return moves

    def get_name(self):
        return 'Q'


class King(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}, op_pieces={}):
        moves = []
        for n in range(-1, 2, 2):
            moves += self.verify_same_team((row, col+n), allied_pieces)
            for c in range(-1, 2):
                moves += self.verify_same_team((row + n, col + c), allied_pieces)
        return moves

    def get_name(self):
        return 'K'
