from itertools import cycle

instruction = cycle(open(0).read().rstrip('\n'))


simulate_rocks = 1000000000000

field = [[2] * 7]


def init_piece(round):
    if round % 5 == 0:
        return [[0,0,1,1,1,1,0]]
    elif round % 5 == 1:
        return [[0,0,0,1,0,0,0],
                [0,0,1,1,1,0,0],
                [0,0,0,1,0,0,0]]
    elif round % 5 == 2:
        return [[0,0,0,0,1,0,0],
                [0,0,0,0,1,0,0],
                [0,0,1,1,1,0,0]]
    elif round % 5 == 3:
        return [[0,0,1,0,0,0,0],
                [0,0,1,0,0,0,0],
                [0,0,1,0,0,0,0],
                [0,0,1,0,0,0,0]]
    else:
        return [[0,0,1,1,0,0,0],
                [0,0,1,1,0,0,0]]


def can_move_right(piece):
    for l in piece:
        for d in range(7):
            if l[d] == 1 and (d >= 6 or l[d+1] == 2):
                return False
    return True


def can_move_left(piece):
    for l in piece:
        for d in range(7):
            if l[d] == 1 and (d == 0 or l[d-1] == 2):
                return False
    return True


def move_piece_right(piece):
    for l in piece:
        for d in range(5, -1, -1):
            if l[d] == 1:
                l[d] -= 1
                l[d+1] += 1


def move_piece_left(piece):
    for l in piece:
        for d in range(1, 7):
            if l[d] == 1:
                l[d] -= 1
                l[d-1] += 1


def down_is_stuck(piece, height):
    for d in range(7):
        for h in range(len(piece)-1, -1, -1):
            if piece[h][d] == 1:
                if h < len(piece) -1:
                    if piece[h+1][d] == 2:
                        return True
                elif h == len(piece)-1 and height >= -1:
                    if field[len(field)-height-2][d] == 2:
                        return True
    return False


def simulate_piece_down(piece, height):
    for d in range(7):
        for h in range(len(piece)):
            if piece[h][d] == 1:
                continue
            if h == len(piece)-1:
                if height >= -1 and field[len(field)-height-2][d] == 2:
                    piece[h][d] = 2
                else:
                    piece[h][d] = 0
            else:
                if piece[h+1][d] == 2:
                    piece[h][d] = 2
                else:
                    piece[h][d] = 0


def fixate_piece(piece, height):
    for l in piece:
        for d in range(7):
            if l[d] == 1:
                l[d] = 2
    for l in piece[::-1]:
        if height >= 0:
            field[len(field)-1-height] = list(l)
            height -= 1
        else:
            field.append(list(l))


jet_count = 10091
jet_idx = 0
lookup = {}

for i in range(simulate_rocks):
    piece_idx = i % 5

    if (jet_idx, piece_idx) in lookup:
        prev_entry = lookup[(jet_idx, piece_idx)]
        period = i - prev_entry[0]
        if i % period == simulate_rocks % period:
            prev_height = prev_entry[1]
            height_diff = (len(field) - 1) - prev_height
            rocks_to_sim = simulate_rocks - i
            periods_to_sim = rocks_to_sim // period
            print(prev_height + height_diff * (1 + periods_to_sim))
            break
    else:
        lookup[(jet_idx, piece_idx)] = (i, len(field) - 1)

    piece = init_piece(i)
    height = -4
    while True:
        instr = next(instruction)
        jet_idx = (jet_idx + 1) % jet_count
        if instr == '>':
            if can_move_right(piece):
                move_piece_right(piece)
        else:
            if can_move_left(piece):
                move_piece_left(piece)
        if down_is_stuck(piece, height):
            fixate_piece(piece, height)
            break
        else:
            simulate_piece_down(piece, height)
            height += 1
