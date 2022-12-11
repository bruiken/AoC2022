reg_x = 1
cur_cycle = 0
res = [['.' for _  in range(40)] for _ in range(6)]
for instr in open(0).read().splitlines():
    is_addx = len(instr) > 4
    for _ in range(2 if is_addx else 1):
        cur_cycle += 1
        if reg_x - 1 <= (cur_cycle-1) % 40 <= reg_x + 1:
            res[(cur_cycle-1) // 40][(cur_cycle-1) % 40] = '#'
    if is_addx:
        _, v = instr.split(' ')
        reg_x += int(v)
print('\n'.join(''.join(l) for l in res))
