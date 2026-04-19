# Write a function sum() to add 1 to 10 numbers recursively.

def sum(num: int) -> int:
    if num == 0:
        return 0
    else:
        return num+sum(num-1)
        
for i in range(0,11):
    print(sum(i))
