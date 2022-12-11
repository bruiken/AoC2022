print(sum((a:=eval(l))[0]<=a[3]and a[2]<=a[1]for l in open(0).read().replace('-',',').split()))
