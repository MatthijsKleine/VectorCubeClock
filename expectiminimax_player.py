"""
The AI Player, also known as Vector
"""


class ExpectiMiniMaxPlayer():
    def __init__(self):
        self.depth = 0
        self.max_depth = 5
        self.known_clocks = dict()

    def do_move(self, clock):
        return self.calculate_next_move(clock)

    def calculate_next_move(self, clock):
        # For every possible move, add the move and it's score to a list
        score_move_pairs = []
        for next_move in clock.get_possible_moves():
            next_score = self.min(clock, next_move)
            score_move_pairs.append((next_score, next_move))

        # If there is no move left return 0, else return the best move
        if not score_move_pairs:
            return 0
        else:
            for move_pair in score_move_pairs:
                move_pair[1]
            highest_score, best_move = max(score_move_pairs)
            return best_move

    def expectimin(self, current_clock, player, steps, depth):
        # Update depth
        depth = depth + 1

        # The next clock is a (deep) copy of the current clock
        next_clock = current_clock.deep_copy()

        # Place move on the next clock
        next_clock.place_move(player, steps)

        # Memoisation
        dict_clock  = next_clock.spots
        if (dict_clock in self.known_clocks):


        # If too deep you lose
        if depth < 8:
            self.known_clocks[dict_clock] = 0
            return 0

        # If it is a win return 10
        if next_clock.check_win(player):
            self.known_clocks[dict_clock] = 10
            return 10

        scores = []
        # Compute the minimum score of all possible moves
        for new_move in next_clock.get_spots():
            #
            scores.append(self.expectimax(()))


        return min_score

    def expectimax(self, clock, move):
        return max_score


""" Wikipedia pseudocode
function expectiminimax(node, depth)
    if node is a terminal node or depth = 0
        return the heuristic value of node
    if the adversary is to play at node
        // Return value of minimum-valued child node
        let α := +∞
        foreach child of node
            α := min(α, expectiminimax(child, depth-1))
    else if we are to play at node
        // Return value of maximum-valued child node
        let α := -∞
        foreach child of node
            α := max(α, expectiminimax(child, depth-1))
    else if random event at node
        // Return weighted average of all child nodes' values
        let α := 0
        foreach child of node
            α := α + (Probability[child] × expectiminimax(child, depth-1))
    return α
"""
