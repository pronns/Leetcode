"""You are given two strings s1 and s2. Your task is to identify the characters that appear in either string but not in both (i.e., characters that are unique to one of the strings). Return the result as a sorted string.

Examples:

Input: s1 = "geeksforgeeks", s2 = "geeksquiz"
Output: "fioqruz"
Explanation: The characters 'f', 'i', 'o', 'q', 'r', 'u', and 'z' are present in either s1 or s2, but not in both.
Input: s1 = "characters", s2 = "alphabets"
Output: "bclpr"
Explanation: The characters 'b', 'c', 'l', 'p', and 'r' are present in either s1 or s2, but not in both.
Input: s1 = "rome", s2 = "more"
Output: ""
Explanation: Both strings contain the same characters, so there are no unique characters. The output is an empty string.
"""

#O(n^2) solution
def uncommonChars(s1, s2):
        #code here
    arr= []
    for char in s1: 
        if char not in s2 and char not in arr:
            arr.append(char)
    for char in s2:
        if char not in s1 and char not in arr:
            arr.append(char)
    arr.sort()
    return ''.join(arr)


s1 = "characters"
s2 = "alphabets"
print(uncommonChars(s1,s2))

#O(Nlogn using sets)

def uncommonChars(s1, s2):
    # Convert strings to sets
    set1 = set(s1)
    set2 = set(s2)
    
    # Find union and intersection
    union = set1 | set2
    intersection = set1 & set2
    
    # Uncommon characters = union - intersection
    uncommon = union - intersection
    
    # Return the sorted result as a string
    return ''.join(sorted(uncommon))


s1 = "characters"
s2 = "alphabets"
print(uncommonChars(s1, s2))