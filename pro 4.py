# Write a program that takes number of rows ‘n’ as input and prints the following pattern, for
# n=4, it is,
# 1
# 10
# 101
# 1010
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j%2==0):
            print(0,end="")
        else:
            print(1,end="")
        # print(j,end="")
    print()
