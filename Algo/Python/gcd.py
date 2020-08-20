#Redo GCD 
def findGCD(a, b):
    # we have denominator, numerator and remainder
    if (a < b):
        d = a; n = b
    else:
        n = a; d = b
    while d >= 1:
        # calculate remainder
        r = n%d
        if (r == 0):
    # return
            return d 
        else:
        # key points of this algorithm
        # the bigger number is n = kd + r
        # if d == lr then n must be klr + r 
        # thus we only need to test if d == lr, 
        # all character represents an integer
            n = d
            d = r

findGCD(6, 26)
