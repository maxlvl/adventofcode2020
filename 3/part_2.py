
from functools import reduce

with open("input.txt") as file:
    map = [line.strip() for line in file.readlines()]

# column, row
slope_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

tree_result = []
for thing in slope_list:
    row, col = 0,0
    treecounter = 0
    while row+1 < len(map):
        col += thing[0]
        row += thing[1]
        if map[row][col % len(map[row])] == '#':
            treecounter += 1
    tree_result.append(treecounter)

print(tree_result)
final_result = reduce((lambda x, y: x*y), tree_result)
print(final_result)
