# Mean Groups
'''
 You are given an array of arrays. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.
 Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element. 

 Example:
 - For
    a = [[3,3,4,2], [4,4], [4,0,3,3], [2,3], [3,3,3]]
    the output should be
    meanGroups(a) = [[0,4], [1], 2,3]]

    - mean(a[0]) = (3+3+4+2) / 4 = 3
    - mean(a[1]) = (4+4) / 2 = 4
    - mean(a[2]) = (4+0+3+3) / 4 = 2.5
    - mean(a[3]) = (2+3) / 2 = 2.5
    - mean(a[4]) = (3+3+3) / 3 = 3
There are three groups of means: those with mean 2.5, 3, and 4. And they form the following groups:
- Arrays with indices 0 and 4 form a group with mean 3
- Arrays with index 1 forms a group with mean 4
- Arrays with indices 2 and 3 form a group with mean 2.5
'''

from statistics import mean

def meanGroups(a):
    dict_of_means = {}
    list_of_means = []
    output_list = []

    # create list of means for each individual list
    for i in a:
        list_of_means.append(mean(i))

    # add items to dictionary with index being key and mean being value
    for i in range(len(list_of_means)):
        dict_of_means[i] = list_of_means[i]

    # create list of which lists share the same mean based on index
    for i in set(dict_of_means.values()):
        output_list.append([k for k,v in dict_of_means.items() if v == i])

    # sort output lists and print result
    output_list.sort()
    print(output_list)


a = [[3, 3, 4, 2], [4, 4], [4, 0, 3, 3], [2, 3], [3, 3, 3]]
meanGroups(a)

