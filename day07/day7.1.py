cur_sizes = [0]
res = 0
for line in open(0).readlines()[1:]:
    fst, *args = line.split()
    if fst == '$':
        if args[0] == 'cd':
            if args[1] == '..':
                if cur_sizes[-1] <= 1e5:
                    res += cur_sizes[-1]
                cur_sizes[len(cur_sizes)-2] += cur_sizes.pop()
            else:
                cur_sizes += [0]
    elif fst != 'dir':
        cur_sizes[-1] += int(fst)
for i in range(len(cur_sizes)-1,-1,-1):
    if cur_sizes[i] <= 1e5:
        res += cur_sizes[i]
    if i > 0:
        cur_sizes[i-1] += cur_sizes.pop()
print(res)
