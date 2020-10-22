

class Piece():
    def __init__(self, white):
        self.white = white

    def verify(self, newcoord, allied_pieces):
        try:
            allied_pieces[newcoord]
        except KeyError:
            return [newcoord]
        else:
            return []


class Pawn(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}):
        if self.white:
            return self.__get_white_moves(row, col, allied_pieces)
        else:
            return self.__get_black_moves(row, col, allied_pieces)

    def __get_white_moves(self, row, col, allied_pieces):
        newcoord = (row - 1, col)
        return self.verify(newcoord, allied_pieces)

    def __get_black_moves(self, row, col, allied_pieces):
        newcoord = (row + 1, col)
        return self.verify(newcoord, allied_pieces)

    def get_name(self):
        return 'P'


class Knight(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}):
        if self.white:
            return self.__get_white_moves(row, col, allied_pieces)
        else:
            return self.__get_black_moves(row, col, allied_pieces)

    def __get_white_moves(self, row, col, allied_pieces):
        moves = []
        for n in range(-1, 2, 2):
            newcoord = (row - 2, col + n)
            moves += self.verify(newcoord, allied_pieces)
        return moves

    def __get_black_moves(self, row, col, allied_pieces):
        return [(row + 2, col + 1), (row + 2, col - 1)]

    def get_name(self):
        return 'k'


class Rook(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}):
        moves = []
        sliding = [True, True, True, True]
        for n in range(1, 8):
            if row + n <= 7:
                if sliding[0]:
                    newcoord = (row + n, col)
                    newmove = self.verify(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        sliding[0] = False
            if row - n >= 0:
                if sliding[1]:
                    newcoord = (row - n, col)
                    newmove = self.verify(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        sliding[1] = False
            if col + n <= 7:
                if sliding[2]:
                    newcoord = (row, col + n)
                    newmove = self.verify(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        sliding[2] = False
            if col - n >= 0:
                if sliding[3]:
                    newcoord = (row, col - n)
                    newmove = self.verify(newcoord, allied_pieces)
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

    def get_moves(self, row, col, allied_pieces={}):
        moves = []
        upright, downright, upleft, downleft = True, True, True, True
        for n in range(1, 8):
            colTopFlag = col + n <= 7
            colBotFlag = col - n >= 0
            if row + n <= 7:
                if colTopFlag and downright:
                    newcoord = (row + n, col + n)
                    newmove = self.verify(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        downright = False
                if colBotFlag and downleft:
                    newcoord = (row + n, col - n)
                    newmove = self.verify(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        downleft = False
            if row - n >= 0:
                if colBotFlag and upleft:
                    newcoord = (row - n, col - n)
                    newmove = self.verify(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        upleft = False
                if colTopFlag and upright:
                    newcoord = (row - n, col + n)
                    newmove = self.verify(newcoord, allied_pieces)
                    if newmove:
                        moves += newmove
                    else:
                        upright = False
        return moves

    def get_name(self):
        return 'B'


class Queen(Piece):
    def __init__(self, white):
        super().__init__(white)

    def get_moves(self, row, col, allied_pieces={}):
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

    def get_moves(self, row, col, allied_pieces={}):
        moves = []
        for n in range(-1, 2, 2):
            moves.append((row, col+n))
            for c in range(-1, 2):
                moves.append((row + n, col + c))
        return moves

    def get_name(self):
        return 'K'