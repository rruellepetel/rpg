#!/usr/bin/env python
# -- coding: UTF-8 --

from core.board import Board, Cell
from core.character import Player


class BoardDisplayer(Board) :
    def __init__(self, board, player):
        self.player = player
        self.board = board

    def display(self, board):
        pass

    def wait_move(self, board):
        pass

    def get_grid(self):
       return self.board.grid    def get_height(self):
       return len(self.board.grid)    def get_width(self):
       return len(self.board.grid[0])

class ConsoleBoard(BoardDisplayer) :
    pass
