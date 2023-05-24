import random
import sys
import heapq

random.seed(10)


class EightPuzzle:
    def __init__(self):
        self.state = None
        self.goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.counter = 0
        self.blank_row = None
        self.blank_col = None
        self.direction = None
        self.moves = []
        self.max_nodes = int(1000000000)

    def setState(self, state):
        self.state = [[int(x) if x != 'b' else 0 for x in row]
                      for row in state.split()]

        for row in range(3):
            for col in range(3):
                if self.state[row][col] == 0:
                    self.blank_row = row
                    self.blank_col = col

    def printState(self):
        if (self.state != None):
            state_str = ''
            for row in self.state:
                for col in row:
                    if col == 0:
                        state_str += 'b'
                    else:
                        state_str += str(col)
                state_str += ' '
            print(state_str[:-1])
            return state_str[:-1]
        else:
            print("No State")
            return ""

    def convertIntoString(self, state):
        state_str = ''
        for row in state:
            for col in row:
                if col == 0:
                    state_str += 'b'
                else:
                    state_str += str(col)
            state_str += ' '
        return state_str[:-1]

    def move(self, direction):
        if direction == 'up' and self.blank_row > 0 and self.state[self.blank_row-1][self.blank_col] != 0:
            # Move up
            self.state[self.blank_row][self.blank_col] = self.state[self.blank_row-1][self.blank_col]
            self.state[self.blank_row-1][self.blank_col] = 0
            self.blank_row -= 1
            return True
        elif direction == 'down' and self.blank_row < 2 and self.state[self.blank_row+1][self.blank_col] != 0:
            # Move down
            self.state[self.blank_row][self.blank_col] = self.state[self.blank_row+1][self.blank_col]
            self.state[self.blank_row+1][self.blank_col] = 0
            self.blank_row += 1
            return True
        elif direction == 'left' and self.blank_col > 0 and self.state[self.blank_row][self.blank_col-1] != 0:
            # Move left
            self.state[self.blank_row][self.blank_col] = self.state[self.blank_row][self.blank_col-1]
            self.state[self.blank_row][self.blank_col-1] = 0
            self.blank_col -= 1
            return True
        elif direction == 'right' and self.blank_col < 2 and self.state[self.blank_row][self.blank_col+1] != 0:
            # Move right
            self.state[self.blank_row][self.blank_col] = self.state[self.blank_row][self.blank_col+1]
            self.state[self.blank_row][self.blank_col+1] = 0
            self.blank_col += 1
            return True
        else:
            # Invalid move
            return False

    def randomizeState(self, n):
        self.setState("b12 345 678")
        directions = ['up', 'down', 'left', 'right']
        i = 0
        while i < n:
            direction = random.choice(directions)
            if self.move(direction):
                i += 1
            else:
                continue

    def h1(self, state):
        misplaced = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for row in range(3):
            for col in range(3):
                if self.state[row][col] != goal_state[row][col]:
                    misplaced += 1
        return misplaced

    def h2(self, state):
        manhattan_distance = 0
        for row in range(3):
            for col in range(3):
                value = state[row][col]
                if value != 0:
                    goal_row = (value - 1) // 3
                    goal_col = (value - 1) % 3
                    distance = abs(goal_row - row) + abs(goal_col - col)
                    manhattan_distance += distance
        return manhattan_distance

    def opposite_direction(self, direction):
        if direction == 'up':
            return 'down'
        elif direction == 'down':
            return 'up'
        elif direction == 'left':
            return 'right'
        elif direction == 'right':
            return 'left'

    def solve(self, heuristic):
        if (heuristic == "h1"):
            # Initialize the search
            frontier = []
            heapq.heappush(frontier, (self.h1(self.state), 0, self.state, []))
            stringOfFirstState = self.convertIntoString(self.state)
            reached = {stringOfFirstState: 0}

            # Initialize the number of nodes reached
            num_nodes_reached = 1

            while frontier:
                # Pop the state with the lowest estimated cost
                _, num_moves, state, moves = heapq.heappop(frontier)
                stringOfState = self.convertIntoString(state)
                self.setState(stringOfState)

                # Check if the goal has been reached
                if self.state == self.goal_state:
                    print(
                        f"Number of nodes Reached for h1: {num_nodes_reached}")
                    print(f"Number of tile moves needed for h1: {len(moves)}")
                    print("Sequence of moves for h1: " + " -> ".join(moves))
                    return True
                    # for experiment purposes
                    # return len(moves)
                    # return num_nodes_reached

                # Expand the state
                for direction in ['up', "down", "right", "left"]:
                    if self.move(direction):
                        new_puzzle = EightPuzzle()
                        new_puzzle.state = [row[:] for row in self.state]
                        new_puzzle.direction = direction
                        string_new_state = new_puzzle.convertIntoString(
                            new_puzzle.state)
                        new_cost = num_moves + 1
                        if (string_new_state not in reached) or (new_cost < reached[string_new_state]):
                            reached[string_new_state] = new_cost
                            # Add the new move to the list of moves
                            new_moves = moves.copy()
                            new_moves.append(direction)
                            heapq.heappush(frontier, (new_puzzle.h1(
                                new_puzzle.state) + new_cost, new_cost, new_puzzle.state, new_moves))
                        self.move(self.opposite_direction(direction))

                # Check if the maximum number of nodes has been reached
                num_nodes_reached = len(reached)
                if num_nodes_reached > self.max_nodes:
                    print(
                        f"Number of nodes Reached for h1: {num_nodes_reached}")
                    print(
                        f"Maximum number of nodes ({self.max_nodes}) reached for h1.")
                    return False

            # No solution found
            return False

        else:
            # Initialize the search
            frontier = []
            heapq.heappush(frontier, (self.h2(self.state), 0, self.state, []))
            stringOfFirstState = self.convertIntoString(self.state)
            reached = {stringOfFirstState: 0}

            # Initialize the number of nodes reached
            num_nodes_reached = 1

            while frontier:
                # Pop the state with the lowest estimated cost
                _, num_moves, state, moves = heapq.heappop(frontier)
                stringOfState = self.convertIntoString(state)
                self.setState(stringOfState)

                # Check if the goal has been reached
                if self.state == self.goal_state:
                    print(
                        f"Number of nodes Reached for h2: {num_nodes_reached}")
                    print(f"Number of tile moves needed for h2: {len(moves)}")
                    print("Sequence of moves for h2: " + " -> ".join(moves))
                    return True
                    # for experiment purposes
                    # return len(moves)
                    # return num_nodes_reached

                # Expand the state
                for direction in ['up', "down", "right", "left"]:
                    if self.move(direction):
                        new_puzzle = EightPuzzle()
                        new_puzzle.state = [row[:] for row in self.state]
                        new_puzzle.direction = direction
                        string_new_state = new_puzzle.convertIntoString(
                            new_puzzle.state)
                        new_cost = num_moves + 1
                        if (string_new_state not in reached) or (new_cost < reached[string_new_state]):
                            reached[string_new_state] = new_cost
                            # Add the new move to the list of moves
                            new_moves = moves.copy()
                            new_moves.append(direction)
                            heapq.heappush(frontier, (new_puzzle.h2(
                                new_puzzle.state) + new_cost, new_cost, new_puzzle.state, new_moves))
                        self.move(self.opposite_direction(direction))

                # Check if the maximum number of nodes has been reached
                num_nodes_reached = len(reached)
                if num_nodes_reached > self.max_nodes:
                    print(
                        f"Number of nodes Reached for h2: {num_nodes_reached}")
                    print(
                        f"Maximum number of nodes ({self.max_nodes}) reached for h2.")
                    return False

            # No solution found
            return False

    def getEvaluation(self):
        manhattan_distance = 0
        for row in range(3):
            for col in range(3):
                value = self.state[row][col]
                if value != 0:
                    goal_row = (value) // 3
                    goal_col = (value) % 3
                    distance = abs(goal_row - row) + abs(goal_col - col)
                    manhattan_distance += distance
        return manhattan_distance

    def getSuccessors(self):
        successors = []

        # Check if the current state is the goal state
        if self.state == self.goal_state:
            return successors

        # Otherwise, get the successors of the current state
        for direction in ['up', 'down', 'left', 'right']:
            if self.move(direction):
                successor = EightPuzzle()
                successor.state = [row[:] for row in self.state]
                stringOfState = self.convertIntoString(successor.state)
                successor.setState(stringOfState)
                successor.direction = direction
                successors.append(successor)

                # Move the blank tile back to its original position
                self.move(self.opposite_direction(direction))
        return successors

    def solveBeam(self, k):
        # Initialize the starting state
        current_puzzle = EightPuzzle()
        current_String = self.convertIntoString(self.state)
        current_puzzle.setState(current_String)
        states = [current_puzzle]

        # Initialize the number of nodes reached
        num_nodes_reached = 1

        # check to see if the state is the goal state
        if (self.state == self.goal_state):
            self.setState("b12 345 678")
            print(f"Number of nodes Reached for beam: {num_nodes_reached}")
            print(f"Number of moves for beam: 0")
            print(f"Sequence of moves for beam: ")
            return True

        # Initialize the beam with the current state
        beam = [(current_puzzle.getEvaluation(), current_puzzle)]

        # Initialize the reached set with the cost of reaching the current state
        reached = {}
        reached[self.convertIntoString(current_puzzle.state)] = 0

        while beam:
            # Select the k best states from the expanded states
            beam = heapq.nsmallest(k, beam, key=lambda x: x[0])

            # Check if the goal state has been reached
            if beam[0][1].state == self.goal_state:
                self.setState("b12 345 678")
                self.moves = beam[0][1].moves
                print(f"Number of nodes reached for beam: {num_nodes_reached}")
                print(f"Number of moves for beam: {len(self.moves)}")
                print(f"Sequence of moves for beam: {' -> '.join(self.moves)}")
                return True
                # for experiment purposes
                # return len(self.moves)
                # return num_nodes_reached

            # Expand the states in the beam
            new_beam = []
            for state in beam:
                successors = state[1].getSuccessors()
                for successor in successors:
                    # Calculate the new cost to reach the successor state
                    new_cost = len(state[1].moves) + 1
                    if self.convertIntoString(successor.state) not in reached or new_cost < reached[self.convertIntoString(successor.state)]:
                        # Set the moves and add the state to the new beam
                        successor.moves = state[1].moves + \
                            [successor.direction]
                        new_beam.append((successor.getEvaluation(), successor))

                        # Add the state to the reached set with the new cost
                        reached[self.convertIntoString(
                            successor.state)] = new_cost

            num_nodes_reached = len(reached)

            # Update the beam with the expanded states
            beam = new_beam

            # Check if maximum number of nodes has been reached
            if num_nodes_reached > self.max_nodes:
                print(f"Number of nodes Reached for beam: {num_nodes_reached}")
                print(
                    f"Maximum number of nodes ({self.max_nodes}) reached for beam.")
                return False

        # No solution found
        return False

    def maxNodes(self, n):
        self.max_nodes = int(n)


if __name__ == '__main__':
    # Parse the input filename from the command line arguments
    if len(sys.argv) != 2:
        print("Usage: python eight_puzzle.py input_file")
        sys.exit(1)
    input_file = sys.argv[1]

    # Read the commands from the input file
    with open(input_file, 'r') as f:
        commands = f.read().splitlines()

    # Create the puzzle object and execute the commands
    puzzle = EightPuzzle()
    for command in commands:
        parts = command.split()
        method = parts[0]
        args = parts[1:]

        if method == 'setState':
            state_str = " ".join(args)
            puzzle.setState(state_str)
        elif method == 'move':
            puzzle.move(*args)
        elif method == 'printState':
            puzzle.printState()
        elif method == 'randomizeState':
            if len(args) == 0:
                puzzle.randomizeState()
            elif len(args) == 1:
                n = int(args[0])
                puzzle.randomizeState(n)
        elif method == 'solve':
            if args[0] == 'A-star':
                input_str = args[-1]
                puzzle.solve(input_str)
            else:
                input_num = int(args[-1])
                puzzle.solveBeam(input_num)
        elif method == 'maxNodes':
            n = int(args[0])
            puzzle.max_nodes = n
