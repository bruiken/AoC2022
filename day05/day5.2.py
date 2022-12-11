s = [
    list('FCPGQR'),
    list('WTCP'),
    list('BHPMC'),
    list('LTQSMPR'),
    list('PHJZVGN'),
    list('DPJ'),
    list('LGPZFJTR'),
    list('NLHCFPTJ'),
    list('GVZQHTCW')
]

for n, f, t in [l.split()[1::2] for l in open(0).readlines()[10:]]:
    n, f, t = int(n), int(f), int(t)
    s[t-1] += s[f-1][-n:]
    s[f-1] = s[f-1][:-n]

print(''.join(l[-1] for l in s))
