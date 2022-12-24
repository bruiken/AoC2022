from collections import defaultdict


inputlines = open(0).read().split()


# Height and width of INNER FIELD!
HEIGHT, WIDTH = len(inputlines) - 2, len(inputlines[0]) - 2

start, end = (1, 0), (WIDTH, HEIGHT + 1)


storms = defaultdict(list)
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3


for y, line in enumerate(inputlines[:-1]):
    if y == 0:
        continue
    for x, val in enumerate(line[:-1]):
        if x == 0:
            continue
        if val == '^':
            storms[(x, y)].append(NORTH)
        elif val == '>':
            storms[(x, y)].append(EAST)
        elif val == 'v':
            storms[(x, y)].append(SOUTH)
        elif val == '<':
            storms[(x, y)].append(WEST)


def process_storm():
    global storms

    new_storms = defaultdict(list)
    for (x, y), directions in storms.items():
        for direction in directions:
            nx, ny = x, y
            if direction == NORTH:
                if y == 1:
                    ny = HEIGHT
                else:
                    ny -= 1
            if direction == EAST:
                if x == WIDTH:
                    nx = 1
                else:
                    nx += 1
            if direction == SOUTH:
                if y == HEIGHT:
                    ny = 1
                else:
                    ny += 1
            if direction == WEST:
                if x == 1:
                    nx = WIDTH
                else:
                    nx -= 1
            new_storms[(nx, ny)].append(direction)
    storms = new_storms


current_queue = {start}
minute = 0
while True:
    if not current_queue:
        exit(1)
    minute += 1
    process_storm()
    next_queue = set()
    for (x, y) in current_queue:
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= WIDTH and (x == 1 or 1 <= ny) and (x == WIDTH or ny <= HEIGHT):
                if (nx, ny) not in storms.keys():
                    next_queue.add((nx, ny))
    if end in next_queue:
        print(minute)
        break
    current_queue = next_queue
