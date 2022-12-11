reg_x = 1
cur_cycle = 0
res = 0
for instr in open(0).read().splitlines():
    is_addx = len(instr) > 4
    for _ in range(2 if is_addx else 1):
        cur_cycle += 1
        if (cur_cycle + 20) % 40 == 0:
            res += cur_cycle * reg_x
    if is_addx:
        _, v = instr.split(' ')
        reg_x += int(v)
print(res)
