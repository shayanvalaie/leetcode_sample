
'''
12. Integer to Roman

Given an integer, convert it to a roman numeral.
'''


def intToRoman(num) -> str:

    symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
               ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
               ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
               ["M", 1000]

               ]  # Create a symbol list mapping symbol to its value

    res = ""  # Open answer variable

    # Go through symList reversed with each symbol and value
    for sym, val in reversed(symList):
        if num // val:  # If our number is divisibile by the value we are on
            # Count = our number divided by our value (Example 1500 = 1)
            count = num // val
            # We want to add to our res the symbol of that value * count
            res += (sym * count)
            num = num % val  # Get the remainder after we are finished with the higher symbol so we can re-do algorithm on a lower symbol
    return res  # Return our res


print(intToRoman(1500))
