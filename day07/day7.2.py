cur_sizes = [0]
dir_sizes = []
for line in open(0).readlines()[1:]:
    fst, *args = line.split()
    if fst == '$':
        if args[0] == 'cd':
            if args[1] == '..':
                dir_sizes.append(cur_sizes[-1])
                cur_sizes[len(cur_sizes)-2] += cur_sizes.pop()
            else:
                cur_sizes += [0]
    elif fst != 'dir':
        cur_sizes[-1] += int(fst)
for i in range(len(cur_sizes)-1,-1,-1):
    dir_sizes.append(cur_sizes[-1])
    if i > 0:
        cur_sizes[i-1] += cur_sizes.pop()

space_needed = 3e7 - (7e7 - dir_sizes[-1])
cur_best, rem_dir = 7e7, -1
for d, s in enumerate(dir_sizes):
    if s >= space_needed:
        if s - space_needed < cur_best:
            cur_best = s - space_needed
            rem_dir = d

print(dir_sizes[rem_dir])
