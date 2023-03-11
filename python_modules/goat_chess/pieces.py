from exceptions import InvalidMoveError

class ChessPiece:
    """A generic chess piece class."""

    def __init__(self):
        pass


    def get_available_moves(self):
        """Returns a list of all possible moves from the current location.
        
        Returns
        -------
        moves : list
            List of possible moves.
        """
        pass


    def move(self, new_loc):
        """Moves this piece to a new location.
        
        Parameters
        ----------
        new_loc : list-like
            Location to move the piece to.
            
        Raises
        ------
        InvalidMoveError
            If the move is invalid.
        """
        pass

class NoPiece(ChessPiece):
    """A dummy class for a piece which does not exist."""

    def __init__(self):
        pass


    def get_available_moves(self):
        """Returns a list of all possible moves from the current location.
        
        Returns
        -------
        moves : list
            List of possible moves. An empty list for a NoPiece
        """

        return []


    def move(self, new_loc):
        """Moves this piece to a new location.
        
        Parameters
        ----------
        new_loc : list-like
            Location to move the piece to.
            
        Raises
        ------
        InvalidMoveError
            If the move is invalid. Which is always for no piece.
        """

        raise InvalidMoveError