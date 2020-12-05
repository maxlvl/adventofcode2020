with open("input.txt") as file:
    map = [line.strip() for line in file.readlines()]

row, col = 0,0

treecounter = 0

while row+1 < len(map):
    row += 1
    col += 3
    if map[row][col % len(map[row])] == '#':
        treecounter += 1
        
print(treecounter)
