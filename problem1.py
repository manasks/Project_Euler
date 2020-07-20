#/usr/bin/python
import results

def problem1():
    DEBUG = None
    sum=0
    for number in range(1000):
        if (number%3==0) or (number%5==0):
            if DEBUG:
                print("Number: ", number)
                print("%3: ",number%3)
                print("%5: ",number%5)
            sum = sum + number
        else:
            continue
    return sum

if __name__ == "__main__":
    problem_result = problem1()
    if problem_result == results.result[1]:
        print("Problem successful. Output: {}".format(problem_result))
    else:
        print("Failed. Output: {}".format(problem_result))