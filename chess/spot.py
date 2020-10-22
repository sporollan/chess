import pieces as p


class Spot():
    def __init__(self, row, col, piece=None):
        white = 0 if row < 3 else 1
        self.__init_piece(row, col, white)
        self.row = row
        self.col = col

    def get_move_array(self, allied_pieces):
        try:
            return self.piece.get_moves(self.row, self.col, allied_pieces)
        except AttributeError:
            return []

    def pop_piece(self):
        piece = self.piece
        self.piece = None
        return piece

    def set_piece(self, piece):
        self.piece = piece

    def __init_piece(self, row, col, white):
        self.piece = None
        if row in (1, 6):
            self.piece = p.Pawn(white)
        elif row in (0, 7):
            if col in (0, 7):
                self.piece = p.Rook(white)
            elif col in (1, 6):
                self.piece = p.Knight(white)
            elif col in (2, 5):
                self.piece = p.Bishop(white)
            elif col == 3:
                self.piece = p.Queen(white)
            elif col == 4:
                self.piece = p.King(white)

    def get_spot(self):
        try:
            return self.piece.get_name()
        except AttributeError:
            return ' '
