# Write a program that takes number of rows ‘n’ as input and prints the following pattern. For
# n=4, it is,
# 1
# 121
# 12321
# 1234321

n=int(input())
for i in range(1,n+1):
    x=int("1"*i)**2
    print(x)