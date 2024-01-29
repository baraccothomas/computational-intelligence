from game import Game, Move, Player

class MinMaxPlayer(Player):
    def __init__(self) -> None:
        """
        A player that uses the MinMax algorithm to make moves.
        """
        super().__init__()

    def make_move(self, game: "Game") -> tuple[tuple[int, int], Move]:
        """
        Makes a move using the MinMax algorithm.

        Args:
            game (Game): The current game state.
        Returns:
            tuple[tuple[int, int], Move]: The selected move represented as a tuple of the starting position and the move direction.
        """
        pass

class GameNode:
    """
    Class representing a node in the game tree.
    """
    def __init__(self, value, children) -> None:
        self.value = value
        self.children = children

class AlphaBetaPruning:
    """
    Class representing the Alpha-Beta Pruning algorithm for game tree search.
    """
    def __init__(self, game_tree) -> None:
        self.game_tree = game_tree
        self.root = game_tree.root
    
    def alpha_beta_search(self, node):
        """
        Performs the Alpha-Beta Pruning search algorithm on the game tree starting from the given node.

        Args:
            node: The starting node for the search.

        Returns:
            The best state found by the search algorithm.
        """
        infinity = float('inf')
        best_val = -infinity
        beta = infinity
        
        successors = self.getSuccessors(node)
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        return best_state

    def max_value(self, node, alpha, beta):
        """
        Performs the max-value step of the Alpha-Beta Pruning algorithm.

        Args:
            node: The current node.
            alpha: The best value found so far for the maximizing player.
            beta: The best value found so far for the minimizing player.

        Returns:
            The maximum value found for the current node.
        """
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = -infinity
        for state in self.getSuccessors(node):
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value
    
    def min_value(self, node, alpha, beta):
        """
        Performs the min-value step of the Alpha-Beta Pruning algorithm.

        Args:
            node: The current node.
            alpha: The best value found so far for the maximizing player.
            beta: The best value found so far for the minimizing player.

        Returns:
            The minimum value found for the current node.
        """
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = infinity
        for state in self.getSuccessors(node):
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    def getSuccessors(self, node):
        """
        Returns the successors of the given node.

        Args:
            node: The node for which to retrieve the successors.

        Returns:
            A list of successor nodes.
        """
        assert node is not None
        return node.children
    
    def isTerminal(self, node):
        """
        Checks if the given node is a terminal node.

        Args:
            node: The node to check.

        Returns:
            True if the node is terminal, False otherwise.
        """
        assert node is not None
        return len(node.children) == 0
    
    def getUtility(self, node):
        """
        Returns the utility value of the given node.

        Args:
            node: The node for which to retrieve the utility value.

        Returns:
            The utility value of the node.
        """
        assert node is not None
        return node.value