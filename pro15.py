# Write a Python program that takes a string as input, finds and prints all the unique substrings
# of the given string in a list in lexicographical order.

in_str=input()
subli=set()
for i in range(len(in_str)):
    for j in range(len(in_str)+1):
        # print(in_str[i:j],i,j)
        if in_str[i:j] not in subli and in_str[i:j] not in ['',' ']:
            # print("in loop")
            subli.add(in_str[i:j])
print(sorted(list(subli)))
