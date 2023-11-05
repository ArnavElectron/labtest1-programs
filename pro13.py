# Write a program that accepts word as input from the user and translates that word into Pig
# Latin. In Pig Latin, words are transformed by moving the first letter to the end and adding
# "ay." For example, "hello" becomes "ellohay."

in_str=input()

out_str=in_str[1:]+in_str[0]+"ay"
print(out_str)