"""

118.Pascals Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

"""

def generate(numRows):
    for i in range(numRows,0,-1):
        for j in range(i,1,-1):
            print(" ", end = "")
        for j in range(numRows-i,-1,-1):
            print("1", end = "")
        for j in range(0,numRows-i):
            print("1", end = "")
        print()

        
generate(5)