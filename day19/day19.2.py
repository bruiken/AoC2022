import re
import functools


blueprints = []

for line in open(0).readlines():
    oroc, croc, obroc, obrcc, groc, grobc = map(int, re.findall(' (\d+) ', line))
    blueprints.append((oroc, croc, obroc, obrcc, groc, grobc))


o = [ ( t - 1 ) * t // 2 for t in range( 32 + 1 ) ]


def odfs(blueprint):
    max_geodes = 0
    max_needed = (max(blueprint[0], blueprint[1], blueprint[2], blueprint[4]), blueprint[3], blueprint[5])

    @functools.cache
    def dfs(minutes_left, robots, currency, blueprint):
        nonlocal max_geodes, max_needed
        
        if minutes_left <= 0:
            return
        ore, clay, obsidian, geodes = currency
        ore_r, clay_r, obs_r, geode_r = robots
        if geodes + geode_r * minutes_left + o[minutes_left] <= max_geodes:
            return
        bought_geode = False
        if ore >= blueprint[4] and obsidian >= blueprint[5]:
            bought_geode = True
            dfs(minutes_left-1, (ore_r, clay_r, obs_r, geode_r+1), (ore-blueprint[4]+ore_r, clay+clay_r, obsidian-blueprint[5]+obs_r, geodes+geode_r), blueprint)
        if not bought_geode and ore_r <= max_needed[0] and ore >= blueprint[0]:
            dfs(minutes_left-1, (ore_r+1, clay_r, obs_r, geode_r), (ore-blueprint[0]+ore_r, clay+clay_r, obsidian+obs_r, geodes+geode_r), blueprint)
        if not bought_geode and clay_r <= max_needed[1] and ore >= blueprint[1]:
            dfs(minutes_left-1, (ore_r, clay_r+1, obs_r, geode_r), (ore-blueprint[1]+ore_r, clay+clay_r, obsidian+obs_r, geodes+geode_r), blueprint)
        if not bought_geode and obs_r <= max_needed[2] and ore >= blueprint[2] and clay >= blueprint[3]:
            dfs(minutes_left-1, (ore_r, clay_r, obs_r+1, geode_r), (ore-blueprint[2]+ore_r, clay-blueprint[3]+clay_r, obsidian+obs_r, geodes+geode_r), blueprint)
        if not bought_geode and not (ore >= blueprint[4] and obsidian >= blueprint[5] and ore >= blueprint[0] and ore >= blueprint[1] and obs_r <= max_needed[2] and ore >= blueprint[2] and clay >= blueprint[3]):
            dfs(minutes_left-1, (ore_r, clay_r, obs_r, geode_r), (ore+ore_r, clay+clay_r, obsidian+obs_r, geodes+geode_r), blueprint)
        max_geodes = max(max_geodes, geode_r + geodes)

    dfs(32, (1, 0, 0, 0), (0, 0, 0, 0), blueprint)
    return max_geodes

res = 1
for blueprint in blueprints[:3]:
    g = odfs(blueprint)
    res *= g

print(res)
