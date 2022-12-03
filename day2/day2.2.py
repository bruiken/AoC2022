print(sum((ord(x)+(o:=ord(y[1]))+2)%3-263+3*o for x,*y in open(0).readlines()))
