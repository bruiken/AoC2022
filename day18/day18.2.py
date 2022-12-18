xs, ys, zs = [], [], []
for line in open(0).read().splitlines():
    x, y, z = map(int, line.split(','))
    xs.append(x)
    ys.append(y)
    zs.append(z)

coords = set(zip(xs, ys, zs))


def try_flood(fx, fy, fz, lim=10):
    global coords

    if (fx, fy, fz) in coords:
        return
    new_coords = set(coords)
    coord_stack = [(fx,fy,fz)]
    limit = lim
    new_coords.add(coord_stack[0])
    while coord_stack:
        if limit <= 0:
            return
        limit -= 1
        cx, cy, cz = coord_stack.pop()
        for dx, dy, dz in [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]:
            new_c = (cx + dx, cy + dy, cz + dz)
            if new_c not in new_coords:
                new_coords.add(new_c)
                coord_stack.append(new_c)
    coords = new_coords

# center of big empty space is around 10, 10, 10
try_flood(10, 10, 10, 1e10)

res = 0
for cx, cy, cz in coords:
    for dx, dy, dz in [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]:
        new_c = (cx + dx, cy + dy, cz + dz)
        if new_c not in coords:
            try_flood(*new_c)
        if new_c not in coords:
            res += 1

print(res)
