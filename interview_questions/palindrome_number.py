# Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

# SOLUTION 1 : Converting to string
# Complexity : Time = O(n) | Space = O(n)

# def is_palindrome(num: int) -> bool:
#   return str(num)[::] == str(num)[::-1]

# print(is_palindrome(121))
# print(is_palindrome(-121))
# print(is_palindrome(10))

#============================================#

# SOLUTION 2 : Without Converting to String
# Complexity : Time = O(n) | Space = O(1)

def is_palindrome(num: int) -> bool:
  if num < 0:
    return False

  rev, org_num = 0, num

  while num>0:
    rev = rev*10 + num%10
    num = num//10

  return org_num == rev

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))
