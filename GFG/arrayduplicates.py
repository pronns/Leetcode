
"""
Docstring for GFG.arrayduplicates
def findDuplicates(self, arr):
        # code here
        dict = {}
        for num in arr:
            dict[num] = 1+dict.get(num,0)
        res = []
        for key in dict.keys():
            if dict[key]==2:
                res.append(key)
        return res

"""


def findDuplicates( arr):
    # code here
    dict = {}
    for num in arr:
        dict[num] = 1+dict.get(num,0)
    res = []
    for key in dict.keys():
        if dict[key]==2:
            res.append(key)
    return res

print(findDuplicates([1,2,4,5,2,4]))

