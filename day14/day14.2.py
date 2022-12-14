solids = set()

greatest_y = 0

for line in open(0).read().splitlines():
    coordinates = line.replace(' -> ', ' ').split()
    p_x, p_y = eval(coordinates[0])
    for coord in coordinates[1:]:
        x, y = eval(coord)
        if p_x == x:  # differ in y
            acc = 1 if p_y > y else -1
            while y != p_y:
                if y > greatest_y:
                    greatest_y = y
                solids.add((x, y))
                y += acc
            solids.add((x, y))
        else:  # differ in x
            if y > greatest_y:
                greatest_y = y
            acc = 1 if p_x > x else -1
            while x != p_x:
                solids.add((x, y))
                x += acc
            solids.add((x, y))
        p_x, p_y = eval(coord)

for x in range(-1000, 1000):
    solids.add((x, greatest_y + 2))

sand_drops = 0
while True:
    sand_drops += 1
    dx, dy = 500, 0

    while True:
        if (dx, dy+1) not in solids:
            dy += 1
        elif (dx-1, dy+1) not in solids:
            dx -= 1
            dy += 1
        elif (dx+1, dy+1) not in solids:
            dx += 1
            dy += 1
        else:
            if dx == 500 and dy == 0:
                print(sand_drops)
                exit(0)
            solids.add((dx, dy))
            break
