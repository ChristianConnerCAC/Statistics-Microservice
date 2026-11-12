import MinMax

# User Story #2
# Given the Statistic Analyzer microservice is running, when I send a request with 
# the values 7, 3, 12, and "apple" and ask for the min and max, then the microservice
# ignores the string "apple" and finds the lowest value, 3, and the highest value, 12.

print("")
print("User Story 2 Test: [7, 3, 12, 'apple']")
secondStory = [[7, 3, 12, "apple"]]
maxValue, minValue = MinMax.minMax(secondStory)
print("Maximum Number: ", int(maxValue), "/ Minimum Number: ", int(minValue))
print("")

# Attribute: Reliability:
# Two requests containing a mix of integers and strings
# Example: [5, 1, apple, 10] and [2, banana, 1 , 4] will
# return the min and max values while ignoring the strings
# without producing an error. Both requests must succeed
# two times in a row.

requestOne = [[5, 1, "apple" , 10]]
requestTwo = [[5, 1, "apple" , 10]]
requestThree = [[2, "banana", 1, 4]]
requestFour = [[2, "banana", 1, 4]]

# Tests:
print("Functional Tests: Reliability")
print("For [5, 1, 'apple', 10]")
maxValue, minValue = MinMax.minMax(requestOne)
print("P1 First Request: Max: ", int(maxValue), "/ Min: ", int(minValue))
maxValue, minValue = MinMax.minMax(requestTwo)
print("P1 Second Request: Max: ", int(maxValue), "/ Min: ", int(minValue))
# Max should be 10, Min should be 1.

print("")
print("For [2, 'banana', 1, 4]")
maxValue, minValue = MinMax.minMax(requestThree)
print("P2 First Request: Max: ", int(maxValue), "/ Min: ", int(minValue))
maxValue, minValue = MinMax.minMax(requestFour)
print("P2 Second Request: Max: ", int(maxValue), "/ Min: ", int(minValue))
# Max should be 4, Min should be 1.