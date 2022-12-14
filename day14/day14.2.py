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

sand_drops = 1
queue = [(500, 0)]
while queue:
    x, y = queue.pop()
    if y < greatest_y + 1:
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            new_coord = (x+dx, y+dy)
            if new_coord not in solids:
                queue.append(new_coord)
                solids.add(new_coord)
                sand_drops += 1

print(sand_drops)
