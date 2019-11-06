# Concatenate Sum
'''
 Given an array of positive integers a, your task is to calculate the sum of every possible a[i] + a[j] where a[i] + a[j] is 
 the concatenation of the string representations of a[i] + a[j] respectively.

 Example:
 For a = [10,2], the output should be concatentationSum(a) = 1344
 - a[0] + a[0] = 10 + 10 = 1010
 - a[0] + a[1] = 10 + 2 = 102
 - a[1] + a[0] = 2 + 10 = 210
 - a[1] + a[1] = 2 + 2 = 22
 So the sum is equal to 1010 + 102 + 210 + 22 = 1344

 - For a = [8] the output should be
 concatenationSum(a) = 88

 There is only one number in a and a[0] + a[0] = 8 + 8 = 88 so the answer is 88.
'''

from itertools import permutations

def concatenateSum(a):
    comb = []
    tot = []

    for i in permutations(a, 2):
        comb.append(i)

    for i in a:
        tup = (i, i)
        comb.append(tup)

    for i in comb:
        tot.append(combine(i))

    print(sum(tot))

def combine(tup):
    temp_string = str(tup[0]) + str(tup[1])
    return int(temp_string)

a = [1, 2, 3]
concatenateSum(a)

b = [10, 2]
concatenateSum(b)

c = [8]
concatenateSum(c)