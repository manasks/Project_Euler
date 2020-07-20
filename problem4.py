#/usr/bin/python
import results
no_of_digits = 3
maxdigitvalue = (10**no_of_digits) - 1
maxvalue = maxdigitvalue**2

def problem4():
    print(maxvalue)
    palindrome = maxvalue
    for palindrome in range(maxvalue,0,-1):
        strnumber = str(palindrome)
        reversenumber = strnumber[::-1]
        if strnumber == reversenumber:
            return palindrome

if __name__ == "__main__":
    problem_result = problem4()
    if problem_result == results.result[4]:
        print("Problem successful. Output: {}".format(problem_result))
    else:
        print("Failed. Output: {}".format(problem_result))