import re
import z3

line_regex = re.compile('[xy]=(-?\d+)')
limit = 4000000
solver = z3.Solver()

find_x, find_y = z3.Ints(['fx', 'fy'])

solver.add(0 <= find_x, 0 <= find_y, limit >= find_x, limit >= find_y)

for line in open(0).readlines():
    bordering_coords = set()
    sx, sy, bx, by = map(int, line_regex.findall(line))
    manhattan_dist = abs(sx - bx) + abs(sy - by)
    solver.add(z3.If(sx - find_x < 0, -(sx - find_x), sx - find_x) + z3.If(sy - find_y < 0, -(sy - find_y), sy - find_y) > manhattan_dist)

if solver.check() == z3.sat:
    model = solver.model()
    print(model[find_x].as_long() * 4000000 + model[find_y].as_long())
