print(sum((a:=eval(l))[0]<=a[2]and a[3]<=a[1]or a[2]<=a[0]and a[1]<=a[3]for l in open(0).read().replace('-',',').split()))
