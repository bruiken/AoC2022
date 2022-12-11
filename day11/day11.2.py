monkey_items = [
    [61],
    [76, 92, 53, 93, 79, 86, 81],
    [91, 99],
    [58, 67, 66],
    [94, 54, 62, 73],
    [59, 95, 51, 58, 58],
    [87, 69, 92, 56, 91, 93, 88, 73],
    [71, 57, 86, 67, 96, 95]
]
monkey_operations = [
    lambda x: x * 11,
    lambda x: x + 4,
    lambda x: x * 19,
    lambda x: x * x,
    lambda x: x + 1,
    lambda x: x + 3,
    lambda x: x + 8,
    lambda x: x + 7,
]
monkey_tests = [
    5, 2, 13, 7, 19, 11, 3, 17
]
monkey_throws = [
    { True: 7, False: 4 },
    { True: 2, False: 6 },
    { True: 5, False: 0 },
    { True: 6, False: 1 },
    { True: 3, False: 7 },
    { True: 0, False: 4 },
    { True: 5, False: 2 },
    { True: 3, False: 1 }
]


monkey_inspections = [0] * len(monkey_items)
mod_val = 1
for t in monkey_tests:
    mod_val *= t

for _ in range(10000):
    for m in range(len(monkey_items)):
        for i in monkey_items[m]:
            monkey_inspections[m] += 1
            worry_level = monkey_operations[m](i) % mod_val
            monkey_items[monkey_throws[m][worry_level % monkey_tests[m] == 0]].append(worry_level)
        monkey_items[m] = []

top_2_monkeys = sorted(monkey_inspections)[-2:]
print(top_2_monkeys[0] * top_2_monkeys[1])
