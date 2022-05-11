# a. Program to add two matrices
def addMatrices(a, b):
    if(len(a) != len(b) or len(a[0]) != len(b[0])):
        return "Matrices must be of same order"
    else:
        result = []
        for i in range(len(a)):
            result.append([])
            for j in range(len(a[0])):
                result[i].append(a[i][j]+b[i][j])
        return result


# Example
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
b = [
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [1, 2, 3, 4]
]

r = addMatrices(a, b)
print("Add of matrices")
print(r)


# b. Program to multiply two matrices
def multiplyMatrices(a, b):
    if(len(a[0]) != len(b)):
        return "Column of first matrix must equal to row of second matrix"
    else:
        r = []
        for i in range(len(a)):
            r.append([])
            for j in range(len(b[0])):
                sum = 0
                for k in range(len(a[0])):
                    sum += a[i][k]*b[k][j]
                r[i].append(sum)
        return r


# Example
a = [
    [1, 2],
    [5, 6],
    [9, 10]
]
b = [
    [5, 6, 7],
    [9, 10, 11],
]

r = multiplyMatrices(a, b)
print("Multiply of matrices")
print(r)


# c. Program to find transpose of matrix
def transpose(a):
    r = []
    for i in range(len(a[0])):
        r.append([])
        for j in range(len(a)):
            r[i].append(a[j][i])
    return r


# Example
print("Transpose")
print(a)
r = transpose(a)
print(r)


# d. Program to subtract matrices
def substractMatrices(a, b):
    if(len(a) != len(b) or len(a[0]) != len(b[0])):
        return "Matrices must be of same order"
    else:
        result = []
        for i in range(len(a)):
            result.append([])
            for j in range(len(a[0])):
                result[i].append(a[i][j]-b[i][j])
        return result


# Example
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
b = [
    [2, -6, 7, 1],
    [9, 1, 1, 12],
    [-4, -2, 11, 4]
]
r = substractMatrices(a, b)
print("Substract of matrices")
print(r)
