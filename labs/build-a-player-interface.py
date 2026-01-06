from abc import ABC, abstractmethod
from random import choice


class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        mv_x, mv_y = choice(self.moves)
        print(f"move by: ({mv_x}, {mv_y})")
        self.position = (self.position[0] + mv_x, self.position[1] + mv_y)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        self.moves.extend([(1, 1), (-1, -1), (-1, 1), (1, -1)])


pa = Pawn()
p1 = pa.make_move()
p2 = pa.make_move()
print("path: ", pa.path)
