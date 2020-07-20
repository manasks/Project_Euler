#/usr/bin/python
def problem1():
    DEBUG = None
    sum=0
    for number in range(1000):
        if (number%3==0) and (number%5==0):
            if DEBUG:
                print("Number: ", number)
                print("%3: ",number%3)
                print("%5: ",number%5)
            sum = sum + number
        else:
            continue
    print("TOTAL sum: ", sum)

if __name__ == "__main__":
    problem1()