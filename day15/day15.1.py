import re

line_regex = re.compile('[xy]=(-?\d+)')
check_y = 2000000
checked_xs = set()
beacon_xs_at_check = set()

for line in open(0).readlines():
    sx, sy, bx, by = map(int, line_regex.findall(line))
    if by == check_y:
        beacon_xs_at_check.add(bx)
    manhattan_dist = abs(sx - bx) + abs(sy - by)
    dist_from_check = abs(sy - check_y)
    if manhattan_dist >= dist_from_check:
        for x in range(manhattan_dist - dist_from_check + 1):
            if x == 0:
                checked_xs.add(sx)
            else:
                checked_xs.add(sx + x)
                checked_xs.add(sx - x)

print(len(checked_xs - beacon_xs_at_check))
