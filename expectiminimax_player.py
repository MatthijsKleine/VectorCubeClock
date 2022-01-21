"""
The AI Player, also known as Vector
"""


class ExpectiMiniMaxPlayer:
    def __init__(self):
        self.depth = 0
        self.max_depth = 5
        self.known_clocks = dict()
        self.times_called = 0

    def do_move(self, clock, player):
        return self.calculate_next_move(clock, player)

    def calculate_next_move(self, clock, player):
        # For every possible move, add the move and it's score to a list
        score_move_pairs = []
        for next_move in clock.get_possible_moves(player):
            next_score = 0
            previous_cube_state = clock.current_cube_state
            for i in range(1, 4):
                clock.current_cube_state = clock.cube_states[i]
                next_score = next_score + self.expecti_min(clock, player, next_move, self.depth)
            score_move_pairs.append((next_score/4, next_move))
            clock.current_cube_state = previous_cube_state

        # If there is no move left return 0, else return the best move
        if not score_move_pairs:
            return 0
        else:
            highest_score, best_move = max(score_move_pairs)
            return best_move

    def expecti_min(self, current_clock, player, steps, depth):
        # Update depth
        depth = depth + 1
        self.times_called = self.times_called + 1
        print(self.times_called)

        # The next clock is a (deep) copy of the current clock
        next_clock = current_clock.deep_copy()

        # Place move on the next clock
        next_clock.place_move(player, steps)

        # Memoisation
        dict_clock = next_clock.spots
        if dict_clock in self.known_clocks:
            return self.known_clocks[dict_clock]

        # If too deep you lose
        if depth < 8:
            self.known_clocks[dict_clock] = -1
            return -1

        # If it is a win return 10
        if next_clock.check_win():
            self.known_clocks[dict_clock] = 1
            return 1

        scores = []
        # Compute the minimum score of all possible moves
        for new_move in next_clock.get_possible_moves():
            scores.append(self.expecti_max(next_clock, player, new_move, depth))
        min_score = min(scores)
        self.known_clocks[dict_clock] = min_score
        return min_score

    def expecti_max(self, current_clock, player, steps, depth):
        # Update depth
        depth = depth + 1
        self.times_called = self.times_called + 1
        print(self.times_called)

        # The next clock is a (deep) copy of the current clock
        next_clock = current_clock.deep_copy()

        # Place move on the next clock
        next_clock.place_move(player, steps)

        # Memoisation
        dict_clock = next_clock.spots
        if dict_clock in self.known_clocks:
            return self.known_clocks[dict_clock]

        # If too deep you win
        if depth < 8:
            self.known_clocks[dict_clock] = 1
            return 10

        # If it is a win return 10
        if next_clock.check_win(player):
            self.known_clocks[dict_clock] = 0
            return 0

        scores = []
        # Compute the minimum score of all possible moves
        for new_move in next_clock.get_possible_moves():
            next_score = 0
            previous_cube_state = current_clock.current_cube_state
            for i in range(1, 4):
                current_clock.current_cube_state = current_clock.cube_states[i]
                next_score = next_score + self.expecti_min(current_clock, player, new_move, self.depth)
            scores.append((next_score / 4, new_move))
            current_clock.current_cube_state = previous_cube_state
        max_score = max(scores)
        self.known_clocks[dict_clock] = max_score
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
