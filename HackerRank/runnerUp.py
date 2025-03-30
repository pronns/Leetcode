"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score."""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max1 = -float('inf')
    max2 = -float('inf')
    for num in arr:
        if num > max1:
            max2 = max1  # Update max2 to be the old max1
            max1 = num  # Update max1 to be the new largest number
        elif num > max2:
            max2 = num  # Update max2 if we find a number larger than current max2 but smaller than max1

    print(max2) 
