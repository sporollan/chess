from spot import Spot


class Board():
    def __init__(self):
        self.board = [[Spot(row, col) for col in range(8)] for row in range(8)]

    def move(self, move):
        row, col = move.move_end[0], move.move_end[1]
        self.board[row][col].set_piece(
                self.board[move.move_start[0]][move.move_start[1]].pop_piece())

    def isPiece(self, row, col, turn):
        try:
            return turn == self.board[row][col].piece.white
        except AttributeError:
            return False

    def get_move_array(self, row, col, white):
        allied_pieces = self.__get_allied_pieces(white)
        return self.board[row][col].get_move_array(allied_pieces)

    def get_board(self, marr=[]):
        board = []
        for line in self.board:
            newline = []
            for s in line:
                newline.append(s.get_spot())
            board.append(newline)
        for s in marr:
            if board[s[0]][s[1]] == ' ':
                board[s[0]][s[1]] = '*'
            else:
                board[s[0]][s[1]] = board[s[0]][s[1]] + '*'
        return board

    def is_check(self, white):
        allied_pieces = self.__get_allied_pieces(white)
        opposite_king = self.__get_opposite_king(white)
        for s in allied_pieces:
            if opposite_king in self.board[s[0]][s[1]].get_move_array(allied_pieces):
                return True
        return False

    def __get_allied_pieces(self, white):
        allied_pieces = {}
        for line in self.board:
            for sp in line:
                if sp.piece:
                    if sp.piece.white == white:
                        allied_pieces[(sp.row, sp.col)] = True
        return allied_pieces

    def __get_opposite_king(self, white):
        for line in self.board:
            for sp in line:
                if sp.piece:
                    if sp.piece.white != white:
                        if sp.piece.get_name() == 'K':
                            return (sp.row, sp.col)