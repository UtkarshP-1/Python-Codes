# Using for loop, write and run a Python program to find factorial from 0 to 10

# Solution 1 : 
def factorial(num):
    if num != 0 :
        return num*factorial(num-1)
    else:
        return 1

for i in range(0,10):
    print(factorial(i))


# Solution 2 :
fact = 1
for i in range(0,10):
    if i == 0:
        print(f'{i} factorial is {fact}')
    else:
        fact = fact*i
        print(f'{i} factorial is {fact}')
