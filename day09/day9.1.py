m_map = {'R': [1, 0], 'D': [0, -1], 'L': [-1, 0], 'U': [0, 1]}
visited = {(0,0)}
hd = [0, 0]
tl = [0, 0]
for l in open(0).read().splitlines():
    d, n = l.split()
    for _ in range(int(n)):
        # move head
        hd[0] += m_map[d][0]
        hd[1] += m_map[d][1]
        # move tail
        if abs(hd[0] - tl[0]) > 1 or abs(hd[1] - tl[1]) > 1:
            tl[0] = hd[0] - m_map[d][0]
            tl[1] = hd[1] - m_map[d][1]
        visited.add((*tl,))
print(len(visited))
