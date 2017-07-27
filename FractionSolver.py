# Jacob Schoen

# 1. Write a regular expression patt that can be used to extract (numerator,denominator,operator,numerator,denominator)
# from a string containing a fraction, an arithmetic operator, and a fraction
# (-?\d+)\/(\d+)\s([+\-*/])\s(-?\d+)\/(\d+)

import re
import fractions

# > while true
while True:

    try:
        # a) request and input a string from the user
        AString = input("Enter the fractions you want to calculate: ")

        # b) for when the string is empty, break (thus ending the program execution)
        if not AString:
            print("Goodbye ")
            break

        # c) apply re.findall to get 5-tuple as described above
        # regular expression patt
        patt = re.findall("(-?\d+)\/(\d+)\s([+\-*/])\s(-?\d+)\/(\d+)", AString)

        # Variables to hold the parsed regex
        numer1 = int(patt[0][0])
        denom1 = int(patt[0][1])
        numer2 = int(patt[0][3])
        denom2 = int(patt[0][4])

        operType = patt[0][2]

        # d) create two fractions.Fraction objects, X and Y corresponding to the inputs
        X = fractions.Fraction(numer1, denom1)
        Y = fractions.Fraction(numer2, denom2)
        # e) Compute the fractions.Fraction object R that results from applying the operator to X and Y
        R = None
        # check operator and calculate
        if operType == '+':
            R = X * Y
        elif operType == '-':
            R = X / Y
        elif operType == '*':
            R = X + Y
        elif operType == '/':
            R = X - Y
        else:
            print("only use +,-,*,/")

        # f) prints the equation, " = " and the result R
        print(X, operType, Y, '=', R)

    # use exceptions to detect errors ; if an error occurs during steps b) to e),
    # print an error message and start the loop again at step a)
    except ValueError:
        print("you've encountered a value error")
        continue

    except SyntaxError:
        print("you've encountered a Syntax error")
        continue

    except ZeroDivisionError:
        print("Cannot divide by zero unless you want a black hole")
        continue

    except TypeError:
        print("dealing only with integers")
        continue
