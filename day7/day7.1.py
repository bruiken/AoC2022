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

print(sum(filter(lambda x: x <= 1e5, dir_sizes.values())))
