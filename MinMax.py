# User Story 2:
# As a user, I want to find the lowest number and highest number in my table,
# so that I can find the two furthest values.

def minMax(furthestValues):
    # An empty list to store the new values without the strings.
    integers = []

    # Then checks each row,
    # and in that row checks each value
    for allRows in furthestValues:
        for indexValue in allRows:

            # When it is checking values:
            # Turns that value into a string.
            # Empty string is then made for the symbols.
            valueCheck = str(indexValue)
            stringCheck = ""

            # Checks symbols:
            # Checks for a "-", if found skips it.
            # Checks for a ".", if found skips it.
            for symbols in valueCheck:
                if symbols != "-":
                    if symbols != ".":
                        stringCheck = stringCheck + symbols

            # .isdigit reads that string saying True for digits (0-9) 
            # and False for words (A-Z).
            if stringCheck.isdigit():

            # Quick run down if value is -10.5
            # removes -, gets 10, removes ., gets 5 = 105 that is a digit!
            # puts -10.5 into the new list.

                # Float takes that string and turns it into
                # an actual number that can have a decimal.
                integers.append(float(indexValue))

    # max then looks at all the values and finds the highest number.
    # min then looks at all the values and finds the lowest number.
    maxValue = max(integers)
    minValue = min(integers)

    # returns the highest and lowest value.
    return maxValue, minValue