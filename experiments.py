import os
import sys
from Eightpuzzle import EightPuzzle

# open the file to redirect stdout
with open('output.txt', 'w') as f:
    # redirect stdout to the file
    sys.stdout = open(os.devnull, 'w')

puzzle = EightPuzzle()
generatedStates = []
numberOfSolveableStatesh1 = 0

for i in range(300):
    puzzle.randomizeState(30)
    generatedStates.append(puzzle.state)

# # number of nodes generated for A* search
# num_nodes_gen_h1 = 0
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     num_nodes_gen_h1 = num_nodes_gen_h1 + puzzle.solve("h1")

# num_nodes_gen_h2 = 0
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     num_nodes_gen_h2 = num_nodes_gen_h2 + puzzle.solve("h2")
    

# # solution length part
# total_sol_length_h1 = 0
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     total_sol_length_h1 = total_sol_length_h1 + puzzle.solve("h1")

# total_sol_length_h2 = 0
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     total_sol_length_h2 = total_sol_length_h2 + puzzle.solve("h2")    

# total_sol_length_beam = 0
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     total_sol_length_beam = total_sol_length_beam + puzzle.solveBeam(15)    
    

# #for max nodes part
# n = [75, 112, 168, 252, 378, 567, 850, 1275, 1912, 2868, 4302, 6453]

# h1_75 = 0
# puzzle.maxNodes(n[0])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_75 += 1

# h1_112 = 0
# puzzle.maxNodes(n[1])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_112 += 1

# h1_168 = 0
# puzzle.maxNodes(n[2])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_168 += 1

# h1_252 = 0
# puzzle.maxNodes(n[3])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_252 += 1

# h1_378 = 0
# puzzle.maxNodes(n[4])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_378 += 1

# h1_567 = 0
# puzzle.maxNodes(n[5])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_567 += 1

# h1_850 = 0
# puzzle.maxNodes(n[6])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_850 += 1

# h1_1275 = 0
# puzzle.maxNodes(n[7])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_1275 += 1

# h1_1912 = 0
# puzzle.maxNodes(n[8])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_1912 += 1

# h1_2868 = 0
# puzzle.maxNodes(n[9])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_2868 += 1

# h1_4302 = 0
# puzzle.maxNodes(n[10])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_4302 += 1

# h1_6453 = 0
# puzzle.maxNodes(n[11])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h1")):
#         h1_6453 += 1


# h2_75 = 0
# puzzle.maxNodes(n[0])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_75 += 1

# h2_112 = 0
# puzzle.maxNodes(n[1])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_112 += 1

# h2_168 = 0
# puzzle.maxNodes(n[2])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_168 += 1

# h2_252 = 0
# puzzle.maxNodes(n[3])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_252 += 1

# h2_378 = 0
# puzzle.maxNodes(n[4])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_378 += 1

# h2_567 = 0
# puzzle.maxNodes(n[5])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_567 += 1

# h2_850 = 0
# puzzle.maxNodes(n[6])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_850 += 1

# h2_1275 = 0
# puzzle.maxNodes(n[7])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_1275 += 1

# h2_1912 = 0
# puzzle.maxNodes(n[8])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_1912 += 1

# h2_2868 = 0
# puzzle.maxNodes(n[9])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_2868 += 1

# h2_4302 = 0
# puzzle.maxNodes(n[10])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_4302 += 1

# h2_6453 = 0
# puzzle.maxNodes(n[11])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solve("h2")):
#         h2_6453 += 1

# beam_75 = 0
# puzzle.maxNodes(n[0])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_75 += 1

# beam_112 = 0
# puzzle.maxNodes(n[1])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_112 += 1

# beam_168 = 0
# puzzle.maxNodes(n[2])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_168 += 1

# beam_252 = 0
# puzzle.maxNodes(n[3])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_252 += 1

# beam_378 = 0
# puzzle.maxNodes(n[4])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_378 += 1

# beam_567 = 0
# puzzle.maxNodes(n[5])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_567 += 1

# beam_850 = 0
# puzzle.maxNodes(n[6])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_850 += 1

# beam_1275 = 0
# puzzle.maxNodes(n[7])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_1275 += 1

# beam_1912 = 0
# puzzle.maxNodes(n[8])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_1912 += 1

# beam_2868 = 0
# puzzle.maxNodes(n[9])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_2868 += 1

# beam_4302 = 0
# puzzle.maxNodes(n[10])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_4302 += 1

# beam_6453 = 0
# puzzle.maxNodes(n[11])
# for state in generatedStates:
#     stringOfState = puzzle.convertIntoString(state)
#     puzzle.setState(stringOfState)
#     if (puzzle.solveBeam(15)):
#         beam_6453 += 1


# reset stdout to the console
sys.stdout = sys.__stdout__
# print(f"For maxNodes 75 - h1: Out of 300 randomly generated states, {h1_75/300} were solvable.")
# print(f"For maxNodes 112 - h1: Out of 300 randomly generated states, {h1_112/300} were solvable.")
# print(f"For maxNodes 168 - h1: Out of 300 randomly generated states, {h1_168/300} were solvable.")
# print(f"For maxNodes 252 - h1: Out of 300 randomly generated states, {h1_252/300} were solvable.")
# print(f"For maxNodes 378 - h1: Out of 300 randomly generated states, {h1_378/300} were solvable.")
# print(f"For maxNodes 567 - h1: Out of 300 randomly generated states, {h1_567/300} were solvable.")
# print(f"For maxNodes 850 - h1: Out of 300 randomly generated states, {h1_850/300} were solvable.")
# print(f"For maxNodes 1275 - h1: Out of 300 randomly generated states, {h1_1275/300} were solvable.")
# print(f"For maxNodes 1912 - h1: Out of 300 randomly generated states, {h1_1912/300} were solvable.")
# print(f"For maxNodes 2868 - h1: Out of 300 randomly generated states, {h1_2868/300} were solvable.")
# print(f"For maxNodes 4302 - h1: Out of 300 randomly generated states, {h1_4302/300} were solvable.")
# print(f"For maxNodes 6453 - h1: Out of 300 randomly generated states, {h1_6453/300} were solvable.")
# print(f"For maxNodes 75 - h2: Out of 300 randomly generated states, {h2_75/300} were solvable.")
# print(f"For maxNodes 112 - h2: Out of 300 randomly generated states, {h2_112/300} were solvable.")
# print(f"For maxNodes 168 - h2: Out of 300 randomly generated states, {h2_168/300} were solvable.")
# print(f"For maxNodes 252 - h2: Out of 300 randomly generated states, {h2_252/300} were solvable.")
# print(f"For maxNodes 378 - h2: Out of 300 randomly generated states, {h2_378/300} were solvable.")
# print(f"For maxNodes 567 - h2: Out of 300 randomly generated states, {h2_567/300} were solvable.")
# print(f"For maxNodes 850 - h2: Out of 300 randomly generated states, {h2_850/300} were solvable.")
# print(f"For maxNodes 1275 - h2: Out of 300 randomly generated states, {h2_1275/300} were solvable.")
# print(f"For maxNodes 1912 - h2: Out of 300 randomly generated states, {h2_1912/300} were solvable.")
# print(f"For maxNodes 2868 - h2: Out of 300 randomly generated states, {h2_2868/300} were solvable.")
# print(f"For maxNodes 4302 - h2: Out of 300 randomly generated states, {h2_4302/300} were solvable.")
# print(f"For maxNodes 6453 - h2: Out of 300 randomly generated states, {h2_6453/300} were solvable.")
# print(f"For maxNodes 75 - beam: Out of 300 randomly generated states, {beam_75/300} were solvable.")
# print(f"For maxNodes 112 - beam: Out of 300 randomly generated states, {beam_112/300} were solvable.")
# print(f"For maxNodes 168 - beam: Out of 300 randomly generated states, {beam_168/300} were solvable.")
# print(f"For maxNodes 252 - beam: Out of 300 randomly generated states, {beam_252/300} were solvable.")
# print(f"For maxNodes 378 - beam: Out of 300 randomly generated states, {beam_378/300} were solvable.")
# print(f"For maxNodes 567 - beam: Out of 300 randomly generated states, {beam_567/300} were solvable.")
# print(f"For maxNodes 850 - beam: Out of 300 randomly generated states, {beam_850/300} were solvable.")
# print(f"For maxNodes 1275 - beam: Out of 300 randomly generated states, {beam_1275/300} were solvable.")
# print(f"For maxNodes 1912 - beam: Out of 300 randomly generated states, {beam_1912/300} were solvable.")
# print(f"For maxNodes 2868 - beam: Out of 300 randomly generated states, {beam_2868/300} were solvable.")
# print(f"For maxNodes 4302 - beam: Out of 300 randomly generated states, {beam_4302/300} were solvable.")
# print(f"For maxNodes 6453 - beam: Out of 300 randomly generated states, {beam_6453/300} were solvable.")
# print(f"For h1: Out of 300 randomly generated states, average solution length: {total_sol_length_h1/300}")
# print(f"For h2: Out of 300 randomly generated states, average solution length: {total_sol_length_h2/300}")
# print(f"For beam: Out of 300 randomly generated states, average solution length: {total_sol_length_beam/300}")
# print(f"For h1: Out of 300 randomly generated states, average number of nodes generated: {num_nodes_gen_h1/300}")
# print(f"For h2: Out of 300 randomly generated states, average number of nodes generated: {num_nodes_gen_h2/300}")

