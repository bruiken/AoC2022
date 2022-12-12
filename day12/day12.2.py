start, end = ord('S'), ord('E')
heights = []
e_x, e_y = 0, 0
for line_y, line in enumerate(open(0).read().split()):
    if 'S' in line:
        line = line.replace('S', 'a')
    if 'E' in line:
        e_y = line_y
        e_x = line.find('E')
        line = line.replace('E', 'z')
    heights.append(list(map(ord, line)))

WIDTH = len(heights[0])
HEIGHT = len(heights)

paths = [[(e_x,e_y)]]
while True:
    new_paths = []
    visited = set()
    for path in paths:
        *_, (x, y) = path
        if heights[y][x] == ord('a'):
            print(len(path)-1)
            exit(0)
        new_coords = set()
        if x > 0:
            new_coords.add((x-1, y))
        if y > 0:
            new_coords.add((x, y-1))
        if x < WIDTH - 1:
            new_coords.add((x+1, y))
        if y < HEIGHT - 1:
            new_coords.add((x, y+1))
        cur_height = heights[y][x]
        for coord in new_coords:
            if coord not in visited and coord not in path:
                if cur_height - heights[coord[1]][coord[0]] <= 1:
                    visited.add(coord)
                    new_paths.append(list(path) + [coord])
        if len(paths) == 0:
            print('no path found!')
            break
    paths = new_paths
