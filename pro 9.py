# Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
# integers from the user and print the transpose of the 2D list(nested list/like matrix).
# Eg 1:- row_col=3 input_lst1= [[1, 5],[2, 7]] Output= [[1, 2],[5, 7]]
row_col=int(input())
li=eval(input())
output=list()
x=list()
for i in range(len(li)):
    for j in range(len(li)):
        x.append(li[j][i])
    output.append(x)
    x=[]
print(output)