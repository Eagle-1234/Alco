"""
@author:Richard Cave, Noureddine tahtahi, Ensar Pasa
@studentnumber: ... , ... , 15247392
@date: 2026-12-02

@description: This program reads a triangle of numbers from standard input,
calculates the maximum path sum from the top to the bottom of the triangle,
and prints the result. The algorithm uses a bottom-up dynamic programming approach to efficiently compute the maximum path sum.
"""
import fileinput

save_all = []

# Convert input into a list of integers
for i, line in enumerate(fileinput.input()):
    line = line.strip()
    numbers = line.split()
    numbers_int = [int(num) for num in numbers]
    save_all.append(numbers_int)

# Calculate maximum path sum using a bottom-up approach
for i in range(len(save_all) - 2, -1, -1):
    for j in range(len(save_all[i])):
        neighbour_left = save_all[i + 1][j]
        neighbour_right = save_all[i + 1][j + 1]

        overwrite_value = save_all[i][j] + max(neighbour_left, neighbour_right)
        save_all[i][j] = overwrite_value

print(save_all[0][0])
