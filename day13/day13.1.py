lines = list(map(eval, (x for x in open(0).read().split() if x)))


RIGHT, WRONG, UNDECIDED = -1, 0, 1


def compare(left, right):
    if type(left) is int:
        if type(right) is int:
            if left < right:
                return RIGHT
            if left > right:
                return WRONG
            return UNDECIDED
        else:
            return compare([left], right)
    else:
        if type(right) is int:
            return compare(left, [right])
        else:
            for l, r in zip(left, right):
                if (r := compare(l, r)) != UNDECIDED:
                    return r
            if len(left) < len(right):
                return RIGHT
            elif len(right) < len(left):
                return WRONG
            return UNDECIDED


c = 0
for idx, i in enumerate(range(0, len(lines), 2)):
    comparison = compare(lines[i], lines[i+1])
    if comparison == RIGHT:
        c += idx + 1

print(c)
