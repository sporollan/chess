import players
from board import Board
from moves import Move


class Game():
    def __init__(self):
        self.players = [players.Human(0), players.Human(1)]
        self.turn = 1
        self.board = Board()
        self.status = 'UNFINISHED'
        self.moves = []
        self.check = False
        self.__prep_move()

    def play(self, spot):
        if self.move_start:
            if spot in self.move_array:
                move = Move(self.players[self.turn], self.move_start, spot)
                self.board.move(move)
                self.moves.append(move)
                self.check = self.board.is_check(self.turn)
                self.turn = 0 if self.turn else 1
            self.__prep_move()
        else:
            if self.board.isPiece(spot[0], spot[1], self.turn):
                self.move_start = spot
                self.move_array = self.board.get_move_array(
                                    spot[0], spot[1], self.turn)
        return self.board.get_board(self.move_array)

    def __prep_move(self):
        self.move_start = None
        self.move_array = []
