# Write a program that takes integer 'n' as the number of elements to be inserted inside a list.
# Accept the integer elements for list, and position 'k' from the user. The program's objective is
# to find and display the kth smallest number from the list. It is important to note that the
# numbers in the list may be repeated, and a simple sorting approach may not yield the correct
# result. The program should handle this case by considering the frequency of each number.
# Eg1:-n=6, lst1=[20,7,15,16,7,8], k=3 output=15
# Eg 2:- n=5,lst1=[5,4,19,9,18], k=8 output=None
n=int(input("n"))
li=[]
output=[]
for i in range(n):
    li.append(int(input("ele")))
k=int(input("k"))
for j in li:
    if j not in output:
        output.append(j)
if k>len(output):
    print("None")
    exit()
output.sort()
print(output[k-1])