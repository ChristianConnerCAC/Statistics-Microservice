# User Story 1:
# As a user, I want to receive the mean, mode, and median when I load my table,
# so that I can get more details about what is going on in my data.

def threeMs(withNumbers):
    # An empty list to store the new values without the strings.
    integers = []

    # Then checks each row,
    # and in that row checks each value.
    for allRows in withNumbers:
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

    # After those checks to verify a digit.

    # Mean:
    # Adds all numbers then divides by how many numbers there are.
    # sum of all integers / how many there are.
    meanAverage = sum(integers) / len(integers)

    # Median:
    # We sort the list to find the middle easier.
    # Then we count how many are in that list.
    integers.sort()
    allIntegers = len(integers)

    # Because if it is even we need to do a bit more.
    # This checks if the list has an even amount.
    # If it does it goes into the middle of the list.
    # Takes the one before and after and divides by 2.
    # Example:
    # [3,3,4,5] = Even amount in the list
    # [3,(3,4),5] = Takes 3 and 4 = 3 + 4 = 7 / 2 = 3.5
    if allIntegers % 2 == 0:
        evenRow = allIntegers // 2
        medianMiddle = (integers[evenRow - 1] + integers[evenRow]) / 2

    else:
        # If it isn't an even list.
        # Then goes into the middle of the list
        # and takes that value as the middle.
        evenRow = allIntegers // 2
        medianMiddle = integers[evenRow]

    # Mode
    # Starts out index 0 the first in the list.
    modeRepeat = integers [0]

    # Then starts the repeat count to 0.
    repeatNumber = 0

    # Then checks each value in that list.
    # The first count starts at 0.
    for indexValue in integers:
        countIntegers = 0

        # Checks the list again.
        # if the number matched with a number already counted.
        # Then adds 1 to the count.
        for checkValue in integers:
            if indexValue == checkValue:
                countIntegers += 1

        # If the repeating number shows up more than another one did.
        # It will update that repeat number to the new count.
        # Then takes that number as the number the showed up more.
        if countIntegers > repeatNumber:
            repeatNumber = countIntegers
            modeRepeat = indexValue

    return meanAverage, medianMiddle, modeRepeat

        