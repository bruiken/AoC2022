import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

xs, ys, zs = [], [], []
for line in open(0).read().splitlines():
    x, y, z = map(int, line.split(','))
    xs.append(x)
    ys.append(y)
    zs.append(z)

ax.scatter(xs, ys, zs, marker='o')

plt.show()
