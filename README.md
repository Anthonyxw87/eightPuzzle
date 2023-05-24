# eightPuzzle
This project aims to solve the classic 8-puzzle problem using artificial intelligence algorithms. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one empty tile. The goal is to rearrange the tiles from a given initial configuration to a desired final configuration by sliding the tiles into the empty space.


## Features
- Implemented a Python-based eight puzzle game.
- Utilized various AI algorithms to solve the 8-puzzle problem.
- Implemented search-based problem-solving techniques, including A-star search and beam search.
- Conducted comprehensive testing and experimentation to evaluate the performance of the algorithms.
- Assessed the algorithms' effectiveness and efficiency in solving the 8-puzzle problem.
- Explored optimal and challenging scenarios to analyze the algorithms' behavior.


### Commands
- **setState()**: Set the puzzle state. The argument specifies the puzzle tile positions
with a sequence of three groups of three digits with the blank tile represented by the letter
‘b’. For example, ‘1b5’ specifies a row with 1 in the left tile, nothing in the middle tile and
5 in the right tile. The goal state for each problem will be ”b12 345 678”.

- **printState** Print the current puzzle state.
- **move(direction)**: Move the blank tile ‘up’, ‘down’, ‘left’, or ‘right’.
- **randomizeState(n)**: Make n random moves from the goal state. Note that the goal state is not reachable from all puzzle states, so this method of randomizing the puzzle ensures that
a solution exists.
- **solve A-star(heuristic)**: Solve the puzzle from its current state using A-star search using
heuristic equal to “h1” or “h2” (see section 3.6 Heuristic Functions of 4th Edition). Briefly,
h1 is the number of misplaced tiles; h2 is the sum of the distances of the tiles from their
goal positions. You are free to try other heuristics, but be sure that they are admissible and
describe them in your writeup. When the goal is found, your code should print the number of tile moves needed to obtain the solution followed by the solution as a sequences of moves (up, down, left, or right) from the starting state to the goal state.

- **solve beam(k)**: Solve the puzzle from its current state by adapting local beam search with k states. You will need to define an evaluation function which you should describe in your writeup. It should have a minimum of zero at the goal state. When the goal is found, print the number of tile moves and solution as for A-star search.

- **maxNodes(n)**: Specifies the maximum number of nodes to be considered during a search. If this limit is exceeded during search an error message should be printed.
