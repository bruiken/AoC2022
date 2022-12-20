class Movable:
    def __init__(self, value) -> None:
        self.value = int(value)
        self.moved = False

l = list(map(Movable, open(0).readlines()))
LEN = len(l)

idx = 0
while idx < LEN:
    obj = l[idx]
    if obj.moved:
        idx += 1
        continue
    new_idx = (idx + obj.value) % (LEN - 1)
    obj.moved = True
    l.pop(idx)
    l.insert(new_idx, obj)

zero_idx = 0
for idx, m in enumerate(l):
    if m.value == 0:
        zero_idx = idx

r = 0
for _ in range(3):
    zero_idx += 1000
    search_idx = zero_idx % LEN
    r += l[search_idx].value
print(r)
