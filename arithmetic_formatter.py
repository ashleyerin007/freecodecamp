import re
# Create a function that receives a list of strings that are arithmetic problems 
# and returns the problems arranged vertically and side-by-side. 
# The function should optionally take a second argument. 
# When the second argument is set to `True`, the answers should be displayed.

def arithmetic_arranger(problems, solve = False):

    # limit of 5 problems
    if(len(problems) > 5):
        return "Error: Too many problems"

    first = ""
    second = ""
    lines = ""
    answer = ""
    string = ""

    # get problem list from problems and loop through them
    for problem in problems:
        #search for values that are digits or + or -, not white space
        if(re.search("[^\s0-9.+-]", problem)):
            # check that problem does not contain multiplication or division
            if(re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        # split by space and grab first part of array
        firstOperand = problem.split(" ")[0]
        # split by space and grab operator
        operator = problem.split(" ")[1]
        # split by space and grab third piece of array
        secondOperand = problem.split(" ")[2]

        # operands have maximum width of 4 digits
        if(len(firstOperand) >= 5 or len(secondOperand) >= 5):
            return "Error: Numbers cannot have more than five digits"

        # holds answer to problem
        result = ""
        if(operator == "+"):
            # parse numbers by casting each operand to an int and then casting the result to a string (reason why)
            result = str(int(firstOperand) + int(secondOperand))
        elif(operator == "-"):
            result = str(int(firstOperand) - int(secondOperand))

        # find lengths to determine which operand has more digits, adding 2 to accomodate max length and operator
        length = max(len(firstOperand), len(secondOperand)) + 2
        # right align first operand
        top = str(firstOperand).rjust(length)
        # right align second line and add one to length to accomdate the operator
        bottom = operator + str(secondOperand).rjust(length-1)
        # empty string
        line = ""
        # right align result and cast it to a string
        res = str(result).rjust(length)
        # dash marks
        for s in range(length):
            line += "-"

        # if the current problem is not the last problem
        if problem != problems[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += line + "    "
            answer += res + "    "
        # if the current problem is the last problem
        else:
            first += top
            second += bottom
            lines += line
            answer += res
        
    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + answer
    else:
        string = first + "\n" + second + "\n" + lines
    return string

    return arranged_problems

print(arithmetic_arranger(['1 + 11', '33 - 2', '34 + 33', '99 + 31']))
