KEY = 811589153

l = list(map(lambda x: int(x) * KEY, open(0).readlines()))
LEN = len(l)
indices = list(range(LEN))
LOOPS = 10

for _ in range(LOOPS):
    for idx in range(LEN):
        indices_idx = indices.index(idx)
        new_idx = (indices_idx + l[idx]) % (LEN - 1)
        indices.pop(indices_idx)
        indices.insert(new_idx, idx)

zero_idx = indices.index(l.index(0))
r = 0
for _ in range(3):
    zero_idx += 1000
    search_idx = zero_idx % LEN
    r += l[indices[search_idx]]
print(r)
