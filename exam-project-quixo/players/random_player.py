import random
from game import Game, Move, Player


class RandomPlayer(Player):
    def __init__(self) -> None:
        """
        A player that makes random moves.
        """
        super().__init__()

    def make_move(self, game: "Game") -> tuple[tuple[int, int], Move]:
        """
        Makes a random move in the game.

        Parameters:
        - game ('Game'): The current game state.

        Returns:
        - tuple[tuple[int, int], Move]: A tuple containing the position to move from and the move to make.
        """
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move
