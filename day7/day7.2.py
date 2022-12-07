from collections import defaultdict

current_dir = ['']
dir_parents = dict()
sub_dirs = defaultdict(list)
dir_sizes = defaultdict(int)

for line in open(0).readlines()[1:]:
    fst, *args = line.split()
    if fst == '$':
        if args[0] == 'cd':
            if args[1] == '..':
                current_dir.pop()
            else:
                current_dir.append(args[1])
    elif fst == 'dir':
        cdir = '/'.join(current_dir)
        adir = cdir + '/' + args[0]
        dir_parents[adir] = cdir
        sub_dirs[cdir].append(adir)
    else:
        cdir = '/'.join(current_dir)
        dir_sizes[cdir] += int(fst)
        tmp = cdir
        while tmp in dir_parents:
            dir_sizes[dir_parents[tmp]] += int(fst)
            tmp = dir_parents[tmp]


outer_size = dir_sizes['']
total_space = 7e7
unused = total_space - outer_size
space_needed = 3e7 - unused
cur_best, rem_dir = total_space, ''
for d, s in dir_sizes.items():
    if s >= space_needed:
        if s - space_needed < cur_best:
            cur_best = s - space_needed
            rem_dir = d

print(dir_sizes[rem_dir])
