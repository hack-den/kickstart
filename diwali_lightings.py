######################
# Created by Vaibhav #
######################

# Google Kickstart Round E 2016
# Diwali Lightings 

def findBlue(pattern, number):
    total, blue = len(pattern), pattern.count("B")

    if number <= len(pattern):
        b = pattern[:number].count("B")
    else:
        q = number // total
        r = number % total

        b = q * blue + pattern[:r].count("B")
    return b

t = int(input())
for t in range(1,t+1):
    p = input()
    s,e = map(int,input().split())

    # subtract the bulbs in first (integer-1)
    # from second integer
    b = findBlue(p,e) - findBlue(p,s-1)
    print("Case #%s: %s" % (t,b))

    
