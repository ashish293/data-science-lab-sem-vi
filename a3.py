# a. Program to swap two elements in a list
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# b. Program to find sum of numbers in a list
def sumAr(arr):
    sum = 0
    for x in arr:
        sum = sum + x
    return sum


# c. Program to find even numbers in a list
def evenAr(arr):
    even = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
    return even


# d. Program to do cumulative sum of a list
def cumulativeSum(arr):
    cumSum = []
    sum = 0
    for x in arr:
        sum = sum + x
        cumSum.append(sum)
    return cumSum


# Example
# a
arr = [1, 2, 3, 4, 5]
swap(arr, 0, 1)
print(arr)

# b
print(sumAr([1, 2, 3, 4, 5]))

# c
print(evenAr([1, 2, 3, 4, 5]))

# d
print(cumulativeSum([4, 5, 6, 7, 8]))
