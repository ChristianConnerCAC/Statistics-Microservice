# User Story 3:
# As a user, I want to see each value in my table listed once,
# so that I can see all the different values without repeats.

def uniqueValues(withValues):
    # Starts an empty list,
    # Keeps track of unique values.
    # Example: [1, 1, 2, 3, 4]
    # uniqueList = [1, 2, 3, 4]
    uniqueList = []

    # Starts an empty list,
    # Keeps track of how many times they appeared.
    # Example: [1, 1, 2, 3, 4]
    # appearList = [2, 1, 1, 1]
    appearList = []

    # Starts an empty list that combines
    # unique values with how many times they have appeared.
    # Example: [1, 1, 2, 3 ,4]
    # fullIndex = [1(1), 2, 3, 4]
    fullIndex = []

    # Then checks each row,
    # and in that row checks each value
    # Starts the first value as unique.
    for allRows in withValues:
        for indexValue in allRows:
            uniqueValue = True

            # This checks the value with values in the unique list.
            # If it isn't already in the list,
            # it adds it to the list.
            for checkValue in uniqueList:
                if indexValue == checkValue:
                    uniqueValue = False
            if uniqueValue == True:
                uniqueList.append(indexValue)
                appearList.append(1)

            # If the value is in the unique list.
            # Then adds 1 to how many times it has appeared.
            else:
                appearList[uniqueList.index(indexValue)] += 1

    # Takes all those values in the unique list.
    # Combines the unique value with how many times it has appeared.
    for indexValue in range(len(uniqueList)):
        if appearList[indexValue] == 1:
            fullIndex.append(f"{uniqueList[indexValue]}")
        else:
            # Removes 1 from the parenthesis because the value
            # on the left is already counted.
            # If 4 shows up 4 times, it counts the original value
            # and puts the extra copies in parentheses.
            # Example: 4, 4, 4, 4 = 4(+1, +1, +1) = 4(3)
            fullIndex.append(f"{uniqueList[indexValue]} ({appearList[indexValue] - 1})")
    return fullIndex