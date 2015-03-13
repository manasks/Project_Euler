#/usr/bin/python

DEBUG = 0
SUM = 0
number1 = 0
number2 = 1
temp = 0

while(temp < 4000000):
    temp = number1 + number2
    number1 = number2
    number2 = temp
    
    print "fibonacci: ",temp

    if temp%2:
        continue
    else:
        print "temp: ",temp
        SUM = SUM + temp

print "TOTAL SUM: ", SUM
