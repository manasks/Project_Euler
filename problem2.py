#/usr/bin/python
import results

def problem2():
    temp=0
    number1 = 0
    number2 = 1
    sum = 0
    while(temp < 4000000):
        temp = number1 + number2
        number1 = number2
        number2 = temp

        if temp%2 != 0:
            continue
        else:
            sum = sum + temp

    return sum

if __name__ == "__main__":
    problem_result = problem2()
    if problem_result == results.result[2]:
        print("Problem successful. Output: {}".format(problem_result))
    else:
        print("Failed. Output: {}".format(problem_result))