# Merge Strings
'''
You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".

You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective strings (fewer occurences means the character is considered smaller). If the number of occurrences is equal, then the characters should be compared in the usual way. If both number of occurrences and characters are equal, you should take the characters from the first string to the result.

Given two strings s1 and s2, return the result of the spacial merge function you are implementing.

For s1 = "dce" and s2 = "cccbd", the output should be mergeStrings(s1, s2) = "dcecccbd"

All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.

For s1 = "super" and s2 = "tower", the output should be mergeStrings(s1, s2) = "stouperwer"

Because in both strings all symbols occur only 1 time, strings are merged as usual.

Strings are all lowercase letters.
'''

import re

def mergeStrings(s1, s2):
    s3 = []
    i = 0
    j = 0

    while i < len(s1) and j < len(s2):
        if len(re.findall(s1[i], s1)) < len(re.findall(s2[j], s2)):
            s3.append(s1[i])
            i += 1
        elif len(re.findall(s1[i], s1)) > len(re.findall(s2[j], s2)):
            s3.append(s2[j])
            j += 1
        else:
            if s1[i] <= s2[j]:
                s3.append(s1[i])
                i += 1
            else:
                s3.append(s2[j])
                j += 1

    while i < len(s1):
        s3.append(s1[i])
        i += 1

    while j < len(s2):
        s3.append(s2[j])
        j += 1

    print(s3)


s1 = "dce"
s2 = "cccbd"
mergeStrings(s1, s2)