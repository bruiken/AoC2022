xs, ys, zs = [], [], []
for line in open(0).read().splitlines():
    x, y, z = map(int, line.split(','))
    xs.append(x)
    ys.append(y)
    zs.append(z)

coords = set(zip(xs, ys, zs))

res = 0
for cx, cy, cz in coords:
    for dx, dy, dz in [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]:
        if (cx + dx, cy + dy, cz + dz) not in coords:
            res += 1

print(res)
