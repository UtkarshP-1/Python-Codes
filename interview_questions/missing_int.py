# Q: You are given a list of integers from 1 to N with one number missing. Write a Python function to find the missing number in the list.
# Input: [1, 2, 4, 6, 3, 7, 8]
# Output: 5

# Solution 1:
Input = [1, 2, 4, 6, 3, 7, 8]

n = len(Input)+1

s = sum(Input)

es = n*(n+1)/2

print(es-s)

# Solution 2:
Input = [1, 2, 4, 6, 3, 7, 8]

Input.sort()

for i,j in enumerate(Input):
    if i+1 != j :
        print(i+1)
        break

