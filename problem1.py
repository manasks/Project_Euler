#/usr/bin/python
DEBUG = 0
SUM = 0
number = 0
for number in range(1,1000):
    if (number%3==0) and (number%5==0):
        if DEBUG:
            print "Number: ", number
            print "%3: ",number%3
            print "%5: ",number%5
        SUM = SUM + number
    else:
        continue
print "TOTAL SUM: ", SUM
