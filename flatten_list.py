# Q. Write a Python function to flatten a nested list. The input list can contain lists within it and the function should return a single list with all the elements.
# Input: [1, [2, 3], 4, [5, [6, 7]]]
# Output: [1, 2, 3, 4, 5, 6, 7]

def flatten_list(nested_list: list) -> list:
    blank_list = []
    for i in nested_list:
        if isinstance(i, list):
            blank_list.extend(flatten_list(i))
        else:
            blank_list.append(i)
    return blank_list

inp = [1, [2, 3], 4, [5, [6, 7]]]

out = flatten_list(inp)

print(out)
