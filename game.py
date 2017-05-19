#!/usr/bin/env python
# -- coding: UTF-8 --

from core.board import Board, Cell
from core.character import *
from core.display import *

board = Board (20, 20)
player = Player (50, 1)
boardDisplayer = ConsoleDisplayer(board, player)
# while True :
#     boardDisplayer.display()
#     new_cell = boardDisplayer.wait_move()
#     player.move(new_cell)
boardDisplayer.display()
