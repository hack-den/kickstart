######################
# Created by Vaibhav #
######################

# Google Kickstart Allocation Problem 2020

t = int(input())

for x in range(1,t+1):
    n,b = map(int,input().split())
    houses = list(map(int,input().split()))
    houses.sort()
    
    y = 0
    for house in houses:
        if b >= house:
            b -= house
            y += 1
        else:
            break
            
    print('Case #%s: %s' % (x,y))
