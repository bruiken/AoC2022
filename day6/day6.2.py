print([(l:=open(0).read()),[i+14 for i in range(len(l))if len(set(l[i:i+14]))==14]][1][0])
