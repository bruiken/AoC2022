reg_x = 1
cur_cycle = 0
res = [['.' for _  in range(40)] for _ in range(6)]
for instr in open(0).read().splitlines():
    if instr == 'noop':
        cur_cycle += 1
        if reg_x - 1 <= (cur_cycle-1) % 40 <= reg_x + 1:
            res[(cur_cycle-1) // 40][(cur_cycle-1) % 40] = '#'
    else:
        _, v = instr.split(' ')
        v = int(v)
        for _ in range(2):
            cur_cycle += 1
            if reg_x - 1 <= (cur_cycle-1) % 40 <= reg_x + 1:
                res[(cur_cycle-1) // 40][(cur_cycle-1) % 40] = '#'
        reg_x += v
print('\n'.join(''.join(l) for l in res))
