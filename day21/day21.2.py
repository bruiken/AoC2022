from z3 import *
import re


functions = dict()
values = dict()
monkeys = dict()


for line in open(0).readlines():
    if m := re.match('^([a-z]{4}): (-?\d+)$', line):
        values[m.group(1)] = int(m.group(2))
        monkeys[m.group(1)] = Int(m.group(1))
    elif m := re.match('^([a-z]{4}): ([a-z]{4}) (.) ([a-z]{4})$', line):
        functions[m.group(1)] = (m.group(2), m.group(4), m.group(3))
        monkeys[m.group(1)] = Int(m.group(1))


s = Solver()
# static values
for m in values:
    if m != 'humn':
        s.add(monkeys[m] == values[m])

# dynamic values
for m in functions:
    n1, n2, op = functions[m]
    if m == 'root':
        s.add(monkeys[n1] == monkeys[n2])
    else:
        if op == '+':
            s.add(monkeys[m] == (monkeys[n1] + monkeys[n2]))
        elif op == '*':
            s.add(monkeys[m] == (monkeys[n1] * monkeys[n2]))
        elif op == '-':
            s.add(monkeys[m] == (monkeys[n1] - monkeys[n2]))
        elif op == '/':
            s.add(monkeys[m] == (monkeys[n1] / monkeys[n2]))


assert s.check() == sat
model = s.model()
print(model[monkeys['humn']])
