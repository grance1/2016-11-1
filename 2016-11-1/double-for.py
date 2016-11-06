for x in ['A','B','C']:
    for y in ['1','2','3']:
        print x + y

for x in [1,2,3,4,5,6,7,8]:
    for y in [0,1,2,3,4,5,6,7,8,9]:
        if x >= y:
            continue
        num = 10 * x + y
        print num

