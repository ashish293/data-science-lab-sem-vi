# a. Program to find the size of tuple
mytuple = (4, 5, 6, 7, 8, 9, 10)
print(len(mytuple))


# b. Program to find Maximum and minimum element in tuple
tupMin, tupMax = min(mytuple), max(mytuple)
print("min", tupMin)
print("max", tupMax)


# c. Program to extract digits from a tuple list
tupTest = ((1, 2), 5, (6, 7, (11, 13)), (8, 9, 10))


def extractDigits(tup):  # recursive function
    myList = []
    for i in tup:
        if type(i) == tuple:
            myList.extend(extractDigits(i))
        else:
            myList.append(i)
    return myList


print(extractDigits(tupTest))


# d. Program to remove tuple of K-length
tupl = [(1, 2, 3), (5, 6, 11, 12), (7, 9, 8), (9, 10)]
k = 2
myList = []
for i in tupl:
    if len(i) != k:
        myList.append(i)
print(myList)
