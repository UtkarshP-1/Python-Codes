# Q. Write a Python function to merge two sorted lists into a single sorted list.
# Example:
# Input: [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Solution 1:
Input1, Input2 = [1, 3, 5], [2, 4, 6]

Input1.extend(Input2)

Input1.sort()

print(Input1)

# Solution 2:
inp = [1, 3, 5], [2, 4, 6]

linp = list(inp)

flatList = [item for sublist in linp for item in sublist]

flatList.sort()

print(flatList)
