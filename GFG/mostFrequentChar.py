def getMaxOccurringChar( s):
    #code here
    dict = {}
    for char in s:
        dict[char]=1+dict.get(char,0)
    max_char = None
    max_freq = -1
    for char in sorted(dict):  # Sorting ensures lexicographical order
        if dict[char] > max_freq:
            max_char = char
            max_freq = dict[char]
    
    return max_char


print(getMaxOccurringChar("asvakjafasfa"))