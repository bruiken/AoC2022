forest = [[int(x) for x in y] for y in open(0).read().split()]


def create_view_map_2d(trees):
    result = [0]*len(trees)
    for i in range(len(trees)):
        for j in range(1, i):
            if trees[i] > trees[i-j]:
                result[i] += 1
            else:
                break
        if i > 0:
            result[i] += 1
    return result


max_left = list(map(create_view_map_2d, forest))
max_right = list(map(create_view_map_2d, [x[::-1] for x in forest]))
max_up = list(map(create_view_map_2d, zip(*forest)))
max_down = list(map(create_view_map_2d, [x[::-1] for x in zip(*forest)]))

WIDTH = len(forest[0])
HEIGHT = len(forest)

max_score = 0
for y, row in enumerate(forest):
    for x, tree in enumerate(row):
        score = max_left[y][x]
        score *= max_right[y][-x-1]
        score *= max_up[x][y]
        score *= max_down[x][-y-1]
        if score > max_score:
            max_score = score

print(max_score)
