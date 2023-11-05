# Write a program that takes an integer 'n' as the number of elements to be inserted inside a list.
# Accept the integer elements for list from the user and an integer 'k' as the desired occurrence
# frequency from the user. The program should remove all elements that do not occur exactly
# 'k' times within the list and print the resulting modified list.
# Eg: n=7, li_lst=[10,20,20,30,40,10,50], k=2 Output=[20,20,10,10]

n=int(input("n"))
li=[]
output=[]
for i in range(n):
    li.append(int(input("ele")))
k=int(input("k"))
for i in li:
    if li.count(i)==k:
        output+=[i]
print(output)