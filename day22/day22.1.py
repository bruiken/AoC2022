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

instructions = []
while m := re.match('^(\d+)([LR]?)', instructions_str):
    instructions_str = instructions_str.replace(m.group(0), '', 1)
    instructions.append((int(m.group(1)), m.group(2)))

pos_x, pos_y, direction = y_start[0], 0, RIGHT


def next_move():
    x, y = pos_x, pos_y
    if direction == RIGHT:
        if pos_x + 1 < y_start[y] + y_length[y]:  # stays within bounds
            return pos_x+1, pos_y
        else:  # loops over to other side
            return y_start[y], pos_y
    elif direction == DOWN:
        if pos_y + 1 < x_start[x] + x_length[x]:  # stays within bounds
            return pos_x, pos_y+1
        else:  # loops over to other side
            return pos_x, x_start[x]
    elif direction == LEFT:
        if pos_x - 1 >= y_start[y]:  # stays within bounds
            return pos_x-1, pos_y
        else:  # loops over to other side
            return y_start[y] + y_length[y] - 1, pos_y
    else:  # direction == UP
        if pos_y - 1 >= x_start[x]:  # stays within bounds
            return pos_x, pos_y-1
        else:
            return pos_x, x_start[x] + x_length[x] - 1


for amount, turn in instructions:
    for _ in range(amount):
        npos_x, npos_y = next_move()
        if field[npos_y][npos_x] == WALL:
            break
        else:
            pos_x = npos_x
            pos_y = npos_y
    direction += 1 if turn == 'R' else -1 if turn == 'L' else 0
    direction %= 4

print((pos_y + 1) * 1000 + 4 * (pos_x + 1) + direction)
