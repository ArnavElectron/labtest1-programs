# Write a program to take inputs of different data type as key input and then the value as its
# data_types name (i.e,. “string”, “integer” or “float”). Store the values in a dictionary with key
# as input and value as data type. Make a sentence with all the inputs which are of string data
# type and display the same. For example, for the dictionary {"hello":"string", 5:"integer",
# “world”: “string”} the sentence is "hello world".

n=int(input("enter number of elements:"))
di=dict()
st=""
for i in range(n):
    x=input("enter datatype")
    if x.lower()=="string":
        y=input("enter data")
        st+=y+" "

    elif x.lower()=="float":
        y=float(input("enter data"))
    elif x.lower()=="integer":
        y=int(input("enter data"))
    else:
        print("Program terminated unknown datatype entered")
        exit()
    di[y]=x

print(di)
print(st)