# a. Program to find sum of all items in a dictionary
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 5}
sum = 0
for i in dict.values():
    sum += i
print("Sum of all items in a dictionary:", sum)


# b. Program to merge two dictionary
dict2 = {1: 'a', 2: 'b', 3: 'c', 3: 'd', 5: 'e'}
dict3 = {}
for i in dict:
    dict3[i] = dict[i]
for i in dict2:
    dict3[i] = dict2[i]
print('dict3', dict3)


dict3 = {**dict, **dict2}  # Found from internet
print('dict3', dict3)


# c. Program to remove all duplicate words in a sentence
sentence = "Hello, I am a developer. I am a developer. I am a developer."
senList = sentence.split()
sentence = set(senList)
sentence = " ".join(sentence)
print('sentence', sentence)   # Changed the order

myAns = ""
for i in senList:
    if i not in myAns:
        myAns += i + " "
print('myAns', myAns)         # Not changed the order
