from spot import Spot


class Board():
    def __init__(self):
        self.board = [[Spot(row, col) for col in range(8)] for row in range(8)]

    def move(self, move):
        pass

    def isPiece(self, row, col, turn):
        return self.board[row][col] is not None

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

    def __get_allied_pieces(self, white):
        allied_pieces = {}
        for line in self.board:
            for sp in line:
                if sp.piece:
                    if sp.piece.white == white:
                        allied_pieces[(sp.row, sp.col)] = True
        return allied_pieces