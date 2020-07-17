t = int(input())
for x in range(1,t+1):
    _ = int(input())
    n = list(map(int,input().split()))

    y = len([x for x in range(1,len(n)-1) if n[x] > n[x+1] and n[x] > n[x-1]])
    print('Case #%s: %s' % (x,y))
