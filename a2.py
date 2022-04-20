# a. Program to find sum of array
def sumAr(arr):
    sum = 0
    for x in arr:
        sum = sum + x
    return sum


# b. Program to reverse an array
def reverseAr(arr):
    rev = []
    for i in range(len(arr)):
        rev.append(arr[len(arr) - i - 1])
    return rev


# c. Program to find largest element of an array
def maxAr(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


# Example
# a
print(sumAr([1, 2, 3, 4, 5]))

# b
print(reverseAr([1, 2, 3, 4, 5]))

# c
print(maxAr([14, 4, 5, 6, 7, 8, 9, 10]))
