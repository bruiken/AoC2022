print([(l:=input()),[i+14 for i in range(len(l))if len({*l[i:i+14]})>13]][1][0])
