#/usr/bin/python

def problem2():
    temp=0
    while(temp < 4000000):
        sum = 0
        number1 = 0
        number2 = 1

        temp = number1 + number2
        number1 = number2
        number2 = temp

        print("fibonacci: ",temp)

        if temp%2:
            continue
        else:
            print("temp: ",temp)
            sum = sum + temp

    print("TOTAL sum: ", sum)

if __name__ == "__main__":
    problem2()