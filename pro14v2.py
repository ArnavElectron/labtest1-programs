in_str=input()
shiftkey=int(input())
out_str=""
for i in in_str:
    if i.isalpha():
        if i.isupper():
            startchar="A"
        else:
            startchar="a"
        x=(ord(i)+shiftkey)-ord(startchar)
        x=x%26
        print(x)
        out_str+=chr(x+ord(startchar))
    else:
        out_str+=i
print(out_str)