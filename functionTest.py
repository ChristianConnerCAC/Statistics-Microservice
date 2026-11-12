import MinMax
import UniqueValues

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

# User Story #3
# Given the Statistics Analyzer microservice is running, when I send a request
# with the repeating values 2, 4, 4, 10, and ask for the unique values, then the
# microservice returns each value only once without repetition: 2, 4, 10.

print("")
print("User Story 3 Test: [2, 4, 4, 10]")
thirdStory = [[2, 4, 4, 10]]
uniqueList = UniqueValues.uniqueValues(thirdStory)
print("Unique: ", uniqueList)

# Attribute: Reliability:
# A request containing integers with repeating values
# for example 1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9
# will return each unique value once and show how many times it repeats
# in parenthesis. The request must succeed 2 times in a row without error.

uniqueOne = [[1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9]]
uniqueTwo = [[1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9]]

print("")
print("Functional Tests: Reliability")
print("For [1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9]")
uniqueList = UniqueValues.uniqueValues(uniqueOne)
print("First Unique Test: ", uniqueList)
uniqueList = UniqueValues.uniqueValues(uniqueTwo)
print("Second Unique Test: ", uniqueList)
# Should give you ['1 (1)', '2', '3', '4 (3)', '5', '6', '7 (2)', '8', '9']