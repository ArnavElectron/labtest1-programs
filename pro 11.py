# Write a program to take inputs of different data type as key input and then the value as its
# data_types name (i.e,. “string”, “integer” or “float”). Store the values in a dictionary with key
# as input and value as data type. Make a sentence with all the inputs which are of string data
# type and display the same. For example, for the dictionary {"hello":"string", 5:"integer",
# “world”: “string”} the sentence is "hello world".

n=int(input())
di=dict()
for i in range(n):
    x=input()
    di[x]=type(x)
print(di)
