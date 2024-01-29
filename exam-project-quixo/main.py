
from game import Game
from players.random_player import RandomPlayer

if __name__ == '__main__':
    g = Game()
    g.print()
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    winner = g.play(player1, player2)
    g.print()
    print(f"Winner: Player {winner}")
