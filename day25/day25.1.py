def to_value(n):
    match n:
        case '-':
            return -1
        case '=':
            return -2
        case d:
            return int(d)


def to_snafu(n):
    return ['0', '1', '2', '=', '-'][n%5]


def get_carry(n):
    if n < -2:
        return -1
    elif n > 2:
        return 1
    else:
        return 0


def combine(n1, n2):
    n1 = n1[::-1]
    n2 = n2[::-1]
    if len(n1) < len(n2):
        n1, n2 = n2, n1
    result = []
    carry = 0
    for idx, d1 in enumerate(n1):
        if idx < len(n2):
            d2 = n2[idx]
        else:
            d2 = '0'
        v1, v2 = to_value(d1), to_value(d2)
        nv = carry + v1 + v2
        carry = get_carry(nv)
        result.append(to_snafu(nv))
    if carry != 0:
        result.append(to_snafu(carry))
    return result[::-1]

lines = open(0).read().split()
r = lines[0]
for c in lines[1:]:
    r = combine(r, c)

print(''.join(r))