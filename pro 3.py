# Write a program that takes number of rows ‘n’ as input and prints the following pattern, for
# n=4, it is,
# ###1
# ##21
# #321
# 4321

n=int(input())
rows=n
for i in range(1,n+1):
    for j in range(rows,i,-1):
        print("#",end="")
    for k in range(i,0,-1):
        print(k,end="")
    print()
        

