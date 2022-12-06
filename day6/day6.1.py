print((l:=input(),*[i+4 for i in range(len(l))if len({*l[i:i+4]})>3])[1])
