# Write a program that takes a sentence as input and converts each alphabet in a given sentence
# to the next letter in the alphabet, while preserving the case of the letters. For example, a is
# converted to b, b to c, so on and z to a. (ignore punctuations in the input sentence) Eg:
# inp_str=”Welcome to python” output=”Xfmdpnf up qzuipm”

in_str=input()
out_str=""
for i in in_str:
    if i.isalpha():
        if i.lower()=="z":
            out_str+=chr(ord(i)-25)
        out_str+=chr(ord(i)+1)
    else:
        out_str+=i
print(out_str)