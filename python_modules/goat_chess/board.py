import numpy as np
from pieces import *

class Board:
    """A chessboard."""


    def __init__(self) -> None:
        
        # Initialize board
        self.board = np.ndarray((8, 8), dtype=ChessPiece)