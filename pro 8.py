# Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
# integers from the user and prints the average of the elements along the main diagonal of the
# 2D list(nested list).
# Eg 1: row_ col= 3, input_lst1=[[1,2,3],[4,5,6],[7,8,9]], output= 5.0 (i.e. (1 + 5 + 9) / 3 =5.0)
row_col=int(input())
li=eval(input())
avgs=0.0
for i in range(row_col):
    avgs+=li[i][i]
print(avgs/row_col)