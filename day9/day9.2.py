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
            cur_x, cur_y = rope[k]
            pre_x, pre_y = rope[k-1]
            dx, dy = abs(pre_x - cur_x), abs(pre_y - cur_y)
            if dx > 1 or dy > 1:
                if dx > 0:
                    rope[k][0] += 1 if pre_x > cur_x else -1
                if dy > 0:
                    rope[k][1] += 1 if pre_y > cur_y else -1
        visited.add((*rope[-1],))
print(len(visited))
