# Problem Statement: Given a number, convert it into the form of words.
#
# Note:- Consider maximum no. of digits in the number as 4.
#
# Examples:
#
# Example 1:
# Input: 7824
# Output: seven thousand eight hundred twenty four
# Explanation: 7824 in words can be written as seven thousand eight hundred twenty four.
#
# Example 2:
# Input: 370
# Output: three hundred seventy
# Explanation: 370 in words can be written as three hundred seventy.

def convert_num_to_words(num):
    # Arrays of strings for handling different cases
    singledigit = ["zero", "one", "two", "three",
                   "four", "five", "six", "seven", "eight", "nine"]
    twodigits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen",
                 "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tensmultiple = ["", "", "twenty", "thirty", "forty",
                    "fifty", "sixty", "seventy", "eighty", "ninety"]
    tenspower = ["hundred", "thousand"]

    # Check if the number is empty
    if len(num) == 0:
        return ""

    # Check if the number is a single digit
    elif len(num) == 1:
        return singledigit[int(num)]

    result = ""  # Initialize the result string
    i = 0  # Initialize index

    while i < len(num):
        # For more than two digits
        if len(num) > 2:
            # Add hundreds place digit and "hundred"
            if num[i] != '0':
                result += singledigit[int(num[i])] + \
                    " " + tenspower[len(num) - 3] + " "
            len -= 1

        # For two digits
        else:
            # If tens place is 1
            if num[i] == '1':
                result += twodigits[int(num[i + 1])] + " "
                return result
            # If tens place is other than 1 and not 0
            elif num[i] != '0':
                result += tensmultiple[int(num[i])] + " "
                if num[i + 1] != '0':
                    result += singledigit[int(num[i + 1])] + " "
                return result
        i += 1

    return result


# Test the function
number = "7824"
print("In words:", convert_num_to_words(number))
