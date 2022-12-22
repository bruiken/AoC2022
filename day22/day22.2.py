import re


lines = open(0).readlines()

field_lines = list(map(lambda x: x.rstrip('\n'), lines[:-2]))
instructions_str = lines[-1].rstrip('\n')

HEIGHT = len(field_lines)
WIDTH = max(len(x) for x in field_lines)

VOID, OPEN, WALL = -1, 0, 1
RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3


field = [[VOID]*WIDTH for _ in range(HEIGHT)]
x_start, x_length = dict(), dict()
y_start, y_length = dict(), dict()
for y, row in enumerate(field_lines):
    row = row.ljust(WIDTH)
    for x, elem in enumerate(row):
        if elem != ' ':
            if y not in y_start:
                y_start[y] = x
            if x not in x_start:
                x_start[x] = y
            if elem == '.':
                field[y][x] = OPEN
            elif elem == '#':
                field[y][x] = WALL
        else:
            if x in x_start and x not in x_length:
                x_length[x] = y - x_start[x]
            if y in y_start and y not in y_length:
                y_length[y] = x - y_start[y]
    if y not in y_length:
        y_length[y] = x - y_start[y] + 1
for x in range(WIDTH):
    if x not in x_length:
        x_length[x] = HEIGHT - x_start[x]


def wrap(px, py, direc):
    if direc == DOWN:
        if 0 <= px < 50:
            return 100 + px, 0, DOWN
        elif 50 <= px < 100:
            return 49, 150 + px - 50, LEFT
        else:  # 100 <= px < 150
            return 99, 50 + px - 100, LEFT
    if direc == LEFT:
        if 0 <= py < 50:
            return 0, 149 - py, RIGHT
        elif 50 <= py < 100:
            return py - 50, 100, DOWN
        elif 100 <= py < 150:
            return 50, 149 - py, RIGHT
        else:  # 150 <= py < 200:
            return py - 100, 0, DOWN
    if direc == UP:
        if 0 <= px < 50:
            return 50, 50 + px, RIGHT
        elif 50 <= px < 100:
            return 0, px + 100, RIGHT
        else:  # 100 <= px < 150
            return px - 100, 199, UP
    if direc == RIGHT:
        if 0 <= py < 50:
            return 99, 149 - py, LEFT
        elif 50 <= py < 100:
            return 50 + py, 49, UP
        elif 100 <= py < 150:
            return 149, 149 - py, LEFT
        else:  # 150 <= py < 200:
            return py - 100, 149, UP


def next_move():
    x, y = pos_x, pos_y
    if direction == RIGHT and pos_x + 1 < y_start[y] + y_length[y]:
        return pos_x+1, pos_y, direction
    elif direction == DOWN and pos_y + 1 < x_start[x] + x_length[x]:
        return pos_x, pos_y+1, direction
    elif direction == LEFT and pos_x - 1 >= y_start[y]:
        return pos_x-1, pos_y, direction
    elif direction == UP and pos_y - 1 >= x_start[x]:
        return pos_x, pos_y-1, direction
    return wrap(pos_x, pos_y, direction)


instructions = []
while m := re.match('^(\d+)([LR]?)', instructions_str):
    instructions_str = instructions_str.replace(m.group(0), '', 1)
    instructions.append((int(m.group(1)), m.group(2)))

pos_x, pos_y, direction = y_start[0], 0, RIGHT

for amount, turn in instructions:
    for _ in range(amount):
        npos_x, npos_y, ndir = next_move()
        if field[npos_y][npos_x] == WALL:
            break
        else:
            pos_x = npos_x
            pos_y = npos_y
            direction = ndir
    direction += 1 if turn == 'R' else -1 if turn == 'L' else 0
    direction %= 4

print((pos_y + 1) * 1000 + 4 * (pos_x + 1) + direction)
