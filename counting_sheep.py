######################
# Created by Vaibhav #
######################

# Google Kickstart Qualification Round
# Counting Sheep

t = int(input())
for t in range(1,t+1):
    x = int(input())

    if x == 0:
        y = "INSOMNIA"
    else:
        digits = [0,1,2,3,4,5,6,7,8,9]
        [digits.remove(int(i)) for i in set(str(x)) if int(i) in digits]

        l = 1
        y = x
        while digits:
            y = x * l
            s = set(str(y))
            [digits.remove(int(i)) for i in s if int(i) in digits]
            l += 1

    print("Case #{x}: {y}".format(x=t, y=y))
