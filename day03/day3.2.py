l=open(0).read().split();print(sum((e:=ord((set(l[i])&set(l[i+1])&set(l[i+2])).pop()))-96+58*(1-e//91) for i in range(0,300,3)))
