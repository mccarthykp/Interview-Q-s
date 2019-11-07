# Remove Vowels from a String
'''
Given a string of n length, remove all of the vowels and return the new string.

Ex. 

remove_vowels("telephone") = "tlphn"
'''

def remove_vowels(s1):
    s2 = ""

    for i in range(len(s1)):
        if s1[i] != "a" and s1[i] != "e" and s1[i] != "i" and s1[i] != "o" and s1[i] != "u":
            s2 = s2 + s1[i]
    print(s2)
    return s2

remove_vowels("telephone")