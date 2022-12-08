forest = [[int(x) for x in y] for y in open(0).read().split()]


def create_max_map_2d(trees):
    left, right = 0, len(trees)-1
    result = list(trees)
    while left < right - 1:
        if result[left] < result[right]:
            left += 1
            result[left] = max(result[left], result[left-1])
        else:
            right -= 1
            result[right] = max(result[right], result[right+1])
    return result


max_x = list(map(create_max_map_2d, forest))
max_y = list(map(create_max_map_2d, zip(*forest)))

WIDTH = len(forest[0])
HEIGHT = len(forest)

res = 0
for y, row in enumerate(forest):
    for x, tree in enumerate(row):
        if (tree == max_x[y][x] or tree == max_y[x][y]) \
            and ((x <= 0 or max_x[y][x-1] < tree) \
                or (x >= WIDTH-1 or max_x[y][x+1] < tree) \
                or (y <= 0 or max_y[x][y-1] < tree) \
                or (y >= HEIGHT-1 or max_y[x][y+1] < tree)):
            res += 1

print(res)
