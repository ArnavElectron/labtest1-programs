# Write a Python program that checks if a given non-negative integer from the user, is a
# palindrome. A palindrome is a number that remains the same when its digits are reversed. For
# example, 121 is a palindrome because it reads the same forward and backward, whereas 1231
# is not a palindrome.

x=str(int(input()))
y=x[::-1]
print(x==y)