print(sum(y-87+(o==y-23)*3+6*((y-o)%3==0)for(o,y)in map(lambda x:map(ord,x.split()),open(0).readlines())))
