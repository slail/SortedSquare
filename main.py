# Sorted Square Algorithm
'''
Write a function that takes a non-empty array
of integers that are sorted in ascending order
and returns a new array of the same length
with the squares of the original integers also
sorted in ascending order.
'''

'''
1. Initialized empty array
2. Traverse though main array
3. Square each element of main array and append to new array in (1)
4. Sort the new array in (1)
'''
# Method 1 - O(nlogn) time | O(n) space
def sortedSquare(array):
    newArr = []
    for value in array:
        newArr.append(value * value)
    newArr.sort()
    return newArr

'''
1. Initialize array of zeros with size of main array
2. Initialize a start and end pointer
3. Traverse through the array in reversed
4. find the larger of the abs value of the "start" and "end"
5. Which ever is larger, it's squared get the position last element position in the array.
6. Move the start or end arrow, from where the is larger in (5).
'''
# Method 2 - O(n) Time | O(n) Space
def sortedSquare1(array):
    newArr = [0 for _ in array]
    smallIndex = 0
    largeIndex = len(array) - 1
    for idx in reversed(range(len(array))):
        smallvalue = array[smallIndex]
        largevalue = array[largeIndex]
        if abs(smallvalue) > abs(largevalue):
            newArr[idx] = smallvalue * smallvalue
            smallIndex += 1
        else:
            newArr[idx] = largevalue * largevalue
            largeIndex -= 1
    return newArr

print(sortedSquare([-4, -2, -1, 0, 2, 5, 8, 19]))
print(sortedSquare1([-4, -2, -1, 0, 2, 5, 8, 19]))
