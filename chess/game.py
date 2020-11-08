import players
import pieces as p
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
        self.check_mate = False
        self.__prep_move()

    def play(self, spot):
        if not self.check_mate:
            if self.move_start:
                if spot in self.move_array:
                    move = Move(self.turn, self.move_start, spot)
                    pawn_promotion = self.board.move(move)
                    self.moves.append(move)
                    if pawn_promotion:
                        self.move_start = spot
                        self.move_array = self.board.get_move_array(spot[0], spot[1], self.turn)
                        return self.board.get_board(self.move_array)
                    self.check = self.board.is_check(self.turn)
                    if self.check:
                        self.check_mate = self.board.is_check_mate(self.turn)
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
