from moves import Move
import pieces as p
import copy

class Board():
    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.board = {1: {(row, col): self.__init_piece(row, col, 1) for col in range(8) for row in range(6, 8)},
                          0: {(row, col): self.__init_piece(row, col, 0) for col in range(8) for row in range(0, 2)}}

    def move(self, move):
        row, col = move.move_end[0], move.move_end[1]
        piece = self.board[move.white].pop((move.move_start[0], move.move_start[1]))
        op = 0 if move.white else 1
        if type(piece) is p.King and piece.can_castle:
            if abs(col - move.move_start[1]) > 1:
                if col == 6:
                    self.board[move.white][(row, 5)] = self.board[move.white].pop((row, 7))
                    self.board[move.white][(row, 5)].can_castle = False
                elif col == 1:
                    self.board[move.white][(row, 2)] = self.board[move.white].pop((row, 0))
                    self.board[move.white][(row, 2)].can_castle = False
            piece.can_castle = False
        pawn_promotion = False
        if type(piece) is p.Pawn:
            pawn_promotion = row in (0, 7)
            piece.en_passant = False
            if piece.move_range == 3:
                piece.move_range = 2
                if abs(row - move.move_start[0]) == 2:
                    piece.en_passant = True
            try:
                if move.white:
                    if self.board[op][(row+1, col)].en_passant:
                        self.__kill_piece(op, row+1, col)
                else:
                    if self.board[op][(row-1, col)].en_passant:
                        self.__kill_piece(op, row-1, col)
            except (KeyError, AttributeError):
                pass
            if col > 7:
                if col == 9:
                    piece = p.Queen(move.white)
                elif col == 10:
                    piece = p.Rook(move.white)
                elif col == 11:
                    piece = p.Bishop(move.white)
                elif col == 12:
                    piece = p.Knight(move.white)
                row, col = move.move_start
        self.__kill_piece(op, row, col)
        if type(piece) is p.Rook:
            piece.can_castle = False
        self.board[move.white][(row, col)] = piece
        return pawn_promotion

    def __kill_piece(self, op, row, col):
        try:
            killed = self.board[op].pop((row, col))
        except KeyError:
            pass

    def isPiece(self, row, col, turn):
        try:
            return self.board[turn][(row, col)] is not None
        except KeyError:
            return False

    def get_move_array(self, row, col, white):
        opposite = 0 if white else 1
        return self.board[white][(row, col)].get_moves(row, col, self.board[white], self.board[opposite])

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
            try:
                if board[m[0]][m[1]] == ' ':
                    board[m[0]][m[1]] = '*'
                else:
                    board[m[0]][m[1]] += '*'
            except IndexError:
                board[4].append(' ')
                board[4] += ['*' for _ in range(4)]


        return board

    def is_check(self, white):
        allied_pieces = self.board[white]
        opposite = 0 if white else 1
        opposite_king = self.get_king(opposite)
        for key in self.board[white]:
            if opposite_king in self.board[white][key].get_moves(key[0], key[1], self.board[white], self.board[opposite]):
                return True
        return False

    def is_check_mate(self, white):
        opposite = 0 if white else 1
        for spot in self.board[opposite]:
            for move in self.board[opposite][spot].get_moves(spot[0], spot[1], self.board[opposite], self.board[white]):
                board = Board(copy.deepcopy(self.board))
                board.move(Move(opposite, spot, move))
                if not board.is_check(white):
                    return False
        return True

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

    def get_king(self, white):
        for key in self.board[white]:
            if self.board[white][key].get_name() == 'K':
                return key

    def __init_piece_by_name(self, n, white):
        white = int(white)
        if n == 'P':
            return p.Pawn(white)
        elif n == 'R':
            return p.Rook(white)
        elif n == 'N':
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
