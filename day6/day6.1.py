print([(l:=open(0).read()),[i+4 for i in range(len(l))if len(set(l[i:i+4]))==4]][1][0])
