# Write a program that takes integer 'n' as the number of elements to be inserted inside a list,
# and the integer elements for list from the user. Modify each element of a list by replacing it
# with the sum of the next two elements. Assume the list is circular, so the last element will be
# the sum of the elements at index[0] and index[1].
# Eg1:-n=4,lst1=[1,2,3,4] output=[5,7,5,3]
# Eg2: n=2, lst1=[100,200], output=[300,300]
n=int(input("n"))
li=[]

for i in range(n):
    li.append(int(input("ele")))
output=[0]*len(li)
for i in range(len(li)):
    idx1=(i+1)%len(li)
    idx2=(i+2)%len(li)
    output[i]=int(li[idx1]+li[idx2])
print("output",output)






# print("len li",len(li))
# print("len out",len(output))
# for i in range(len(li)):
#     # print(i)
#     if i==len(li)-1:
#         output[i]=int(li[0]+li[1])
#         # print("if 1")
#     elif i==len(li)-2:
#         output[i]=int(li[-1]+li[0])
#         # print("if 2")
#     else:
#         output[i]=int(li[i+1]+li[i+2])
#         # print(output)