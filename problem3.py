#/usr/bin/python
import results

def problem3():
    value = 600851475143
    factors = []
    d = 2
    while value > 1:
        while value % d == 0:
            factors.append(d)
            value /= d
        d = d + 1

    return max(factors)

if __name__ == "__main__":
    problem_result = problem3()
    if problem_result == results.result[3]:
        print("Problem successful. Output: {}".format(problem_result))
    else:
        print("Failed. Output: {}".format(problem_result))