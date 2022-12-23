from collections import defaultdict
from itertools import product


ROUNDS = 10
NORTH, SOUTH, WEST, EAST = 0, 1, 2, 3


elf_coordinates = dict()
elf_count = 0
for y, row in enumerate(open(0).read().split()):
    for x, val in enumerate(row):
        if val == '#':
            elf_coordinates[elf_count] = (x, y)
            elf_count += 1


def elf_wants_movement(elf):
    elf_x, elf_y = elf_coordinates[elf]
    for dx, dy in product([-1,0,1], [-1,0,1]):
        if dx == 0 and dy == 0:
            continue
        if (elf_x + dx, elf_y + dy) in current_elf_positions:
            return True
    return False


checks = [
    [[-1, -1], [0, -1], [1, -1]],
    [[-1, 1], [0, 1], [1, 1]],
    [[-1, -1], [-1, 0], [-1, 1]],
    [[1, -1], [1, 0], [1, 1]]
]

def can_move(elf, direction):
    elf_x, elf_y = elf_coordinates[elf]
    if all((elf_x + dx, elf_y + dy) not in current_elf_positions for dx, dy in checks[direction]):
        dx, dy = checks[direction][1]
        return (elf_x + dx, elf_y + dy)


movement_dir = NORTH
for _ in range(ROUNDS):
    current_elf_positions = set(elf_coordinates.values())
    proposed_move_map = defaultdict(list)
    for elf in elf_coordinates:
        if elf_wants_movement(elf):
            for dd in range(4):
                if nc := can_move(elf, (movement_dir + dd) % 4):
                    proposed_move_map[nc].append(elf)
                    break
    for c in proposed_move_map:
        if len(proposed_move_map[c]) == 1:
            elf_coordinates[proposed_move_map[c][0]] = c
    movement_dir = (movement_dir + 1) % 4

min_x, max_x, min_y, max_y = 999, -999, 999, -999
for x, y in elf_coordinates.values():
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

print((max_x - min_x + 1) * (max_y - min_y + 1) - len(elf_coordinates))
