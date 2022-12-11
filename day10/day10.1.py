reg_x = 1
cur_cycle = 0
res = 0
for instr in open(0).read().splitlines():
    if instr == 'noop':
        cur_cycle += 1
        if (cur_cycle + 20) % 40 == 0:
            res += cur_cycle * reg_x
    else:
        _, v = instr.split(' ')
        v = int(v)
        for _ in range(2):
            cur_cycle += 1
            if (cur_cycle + 20) % 40 == 0:
                res += cur_cycle * reg_x
        reg_x += v
print(res)
