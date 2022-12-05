import re
chars = [x for x in range(ord('A'), ord('Z')+1)]

grid = [[] for x in range(9)]
with open('input.txt') as fh:
    for line in fh:
        if not line.strip():
            break
        # print(line, len(line))
        for i, char in enumerate(line.rstrip()):
            if ord(char) in chars:
                # print(i, (i//4))
                grid[i//4].append(char)

    print(grid)
    grid1 = [x[:] for x in grid] # part 1
    grid2 = [x[:] for x in grid] # part 2
    del grid
    for moves in fh:
        # move_re = re.search('move 4 from 9 to 1', moves)
        move_re = re.search('move (\d+) from (\d+) to (\d+)', moves.rstrip())
        n, from_col, to_col = int(move_re.group(1)), int(move_re.group(2)), int(move_re.group(3))
        # print(moves, n, from_col, to_col)
        
        #part 1
        for i in range(n):
            crate = grid1[from_col-1].pop(0)
            grid1[to_col-1].insert(0, crate)

        # part 2
        crates = grid2[from_col-1][:n]
        grid2[from_col-1] = grid2[from_col-1][n:]
        grid2[to_col-1] = crates + grid2[to_col-1]

print(''.join([x[0] for x in grid1]))
print(''.join([x[0] for x in grid2]))
