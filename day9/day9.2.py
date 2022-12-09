m_map = {'R': [1, 0], 'D': [0, -1], 'L': [-1, 0], 'U': [0, 1]}
visited = {(0,0)}
rope = [[0,0] for _ in range(10)]

for l in open(0).read().splitlines():
    d, n = l.split()
    for _ in range(int(n)):
        # move head
        rope[0][0] += m_map[d][0]
        rope[0][1] += m_map[d][1]
        # move tail elements
        for k in range(1, len(rope)):
            if abs(rope[k-1][0] - rope[k][0]) > 1 or abs(rope[k-1][1] - rope[k][1]) > 1:
                if abs(rope[k-1][0] - rope[k][0]) > 0:
                    rope[k][0] = (rope[k][0]+1) if rope[k-1][0] > rope[k][0] else (rope[k][0]-1)
                if abs(rope[k-1][1] - rope[k][1]) > 0:
                    rope[k][1] = (rope[k][1]+1) if rope[k-1][1] > rope[k][1] else (rope[k][1]-1)
        visited.add((*rope[-1],))
print(len(visited))
