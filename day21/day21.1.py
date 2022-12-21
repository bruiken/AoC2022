import re
import operator


functions = dict()
values = dict()


def char_to_op(val):
    if val == '/':
        return operator.floordiv
    if val == '+':
        return operator.add
    if val == '-':
        return operator.sub
    if val == '*':
        return operator.mul


for line in open(0).readlines():
    if m := re.match('^([a-z]{4}): (-?\d+)$', line):
        values[m.group(1)] = int(m.group(2))
    elif m := re.match('^([a-z]{4}): ([a-z]{4}) (.) ([a-z]{4})$', line):
        functions[m.group(1)] = (m.group(2), m.group(4), char_to_op(m.group(3)))


def find_value(name):
    if name in values:
        return values[name]
    n1, n2, op = functions[name]
    v1, v2 = find_value(n1), find_value(n2)
    res = op(v1, v2)
    values[name] = res
    return res


print(find_value('root'))
