# Write a python program that accepts two inputs as word from the user and checks if two
# words are anagrams of each other. An anagram is a word or phrase formed by rearranging the
# letters of another.
# Eg 1: inp_string 1: anagram inp_string 2: nagaram , Output: True
# Eg 2: inp_string 1: baseball, inp_string 2: basketball , Output: False

str1=input()
str2=input()
str1=list(str1)
str2=list(str2)
str1.sort()
str2.sort()
bol=True
if len(str1)!=len(str2):
    print("False")
    exit()
for i in range(len(str1)):
    if str1[i]!=str2[i]:
        bol=False
        break
print(bol)
