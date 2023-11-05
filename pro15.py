# Write a Python program that takes a string as input, finds and prints all the unique substrings
# of the given string in a list in lexicographical order.

in_str=input()
subli=list()
# print(in_str)
# print(len(in_str))
for i in range(len(in_str)):
    for j in range(len(in_str)+1):
        # print(in_str[i:j],i,j)
        if in_str[i:j] not in subli:
            # print("in loop")
            subli.append(in_str[i:j])
subli.remove(" ")
subli.remove('')




print(subli)
subli.sort()