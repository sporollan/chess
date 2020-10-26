from spot import Spot
import pieces as p


class Board():
    def __init__(self):
        self.board = {1: {(row, col): self.__init_piece(row, col, 1) for col in range(8) for row in range(6, 8)},
                        0: {(row, col): self.__init_piece(row, col, 0) for col in range(8) for row in range(0, 2)}}

    def move(self, move):
        row, col = move.move_end[0], move.move_end[1]
        piece = self.board[move.white].pop((move.move_start[0], move.move_start[1]))
        self.board[move.white][(move.move_end[0], move.move_end[1])] = piece

    def isPiece(self, row, col, turn):
        try:
            return self.board[turn][(row, col)] is not None
        except KeyError:
            return False

    def get_move_array(self, row, col, white):
        allied_pieces = self.board[white]
        return self.board[white][(row, col)].get_moves(row, col, allied_pieces)

    def get_board(self, marr=[]):
        board = []
        for row in range(8):
            newline = []
            for col in range(8):
                for white in range(2):
                    try:
                        newline += self.board[white][(row, col)].get_name()
                        empty_flag = 0
                        break
                    except (KeyError, AttributeError):
                        empty_flag = 1
                if empty_flag:
                    newline.append(' ')
            board.append(newline)
        for m in marr:
            if board[m[0]][m[1]] == ' ':
                board[m[0]][m[1]] = '*'
            else:
                board[m[0]][m[1]] += '*'
        return board

    def is_check(self, white):
        allied_pieces = self.board[white]
        opposite_king = self.__get_opposite_king(white)
        for key in self.board[white]:
            if opposite_king in self.board[white][key].get_moves(key[0], key[1], allied_pieces):   #piece.get_moves(allied_pieces):
                return True
        return False

    def set_custom_board(self, board):
        self.board = {1: {}, 0: {}}
        for row, line in enumerate(board):
            for col, p in enumerate(line):
                if len(p) == 2:
                    self.board[int(p[1])][(row, col)] = self.__init_piece_by_name(p[0], p[1])

    def __get_allied_pieces(self, white):
        allied_pieces = {}
        for line in self.board:
            for sp in line:
                if sp.piece:
                    if sp.piece.white == white:
                        allied_pieces[(sp.row, sp.col)] = True
        return allied_pieces

    def __get_opposite_king(self, white):
        for key in self.board[white]:
            if self.board[white][key].get_name() == 'K':
                return key

    def __init_piece_by_name(self, n, white):
        if n == 'P':
            return p.Pawn(white)
        elif n == 'R':
            return p.Rook(white)
        elif n == 'k':
            return p.Knight(white)
        elif n == 'B':
            return p.Bishop(white)
        elif n == 'Q':
            return p.Queen(white)
        elif n == 'K':
            return p.King(white)

    def __init_piece(self, row, col, white):
        piece = None
        if row in (1, 6):
            piece = p.Pawn(white)
        elif row in (0, 7):
            if col in (0, 7):
                piece = p.Rook(white)
            elif col in (1, 6):
                piece = p.Knight(white)
            elif col in (2, 5):
                piece = p.Bishop(white)
            elif col == 3:
                piece = p.Queen(white)
            elif col == 4:
                piece = p.King(white)
        return piece
