import re

line_regex = re.compile('^Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$')

valves = []
minutes = 30

for line in open(0).readlines():
    m = line_regex.match(line)
    valve, flow_rate, tunnels = m.groups()
    flow_rate = int(flow_rate)
    tunnels = tunnels.split(', ')
    valves.append((valve, flow_rate, tunnels))


v_idx = {valve[0]: i for i, valve in enumerate(valves)}
flows = {valve[0]: valve[1] for valve in valves if valve[1] > 0}
distances = [[99]*len(valves) for _ in range(len(valves))]
for valve in valves:
    for tunnel in valve[2]:
        distances[v_idx[valve[0]]][v_idx[tunnel]] = 1
        distances[v_idx[tunnel]][v_idx[valve[0]]] = 1


for i in range(len(valves)):
    for j in range(len(valves)):
        for k in range(len(valves)):
            distances[j][k] = min(distances[j][i] + distances[i][k], distances[j][k])


def dfs(time_left, current_valve, closed_valves):
    best = 0
    for v in closed_valves:
        dist = distances[v_idx[current_valve]][v_idx[v]]
        if dist < time_left:
            remaining_mins = time_left - dist - 1
            pressure_released = remaining_mins * flows[v]
            rest_pressure = dfs(remaining_mins, v, closed_valves - {v})
            if pressure_released + rest_pressure > best:
                best = pressure_released + rest_pressure
    return best

print(dfs(minutes, 'AA', set(flows)))
