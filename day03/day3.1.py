print(sum((e:=ord((set(x[(o:=len(x)//2):])&set(x[:o])).pop()))-96+58*(1-e//91)for x in open(0).readlines()))
