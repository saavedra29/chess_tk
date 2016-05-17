class Piece():
    def __init__(self, color):
        if color == 'black':
            self.shortName = self.shortName.lower()
        elif color == 'white':
            self.shortName = self.shortName.upper()
        self.color = color

    def ref(self, board):
        self.board = board


class King(Piece): shortName = 'k'
