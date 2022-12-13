from functools import cmp_to_key


RIGHT, UNDECIDED, WRONG = 1, 0, -1
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


lines = list(map(eval, (x for x in open(0).read().split() if x))) + [[[2]], [[6]]]
lines = sorted(lines, key=cmp_to_key(compare))[::-1]
print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))
