# A cipher is a method of transforming a message to conceal its meaning. The simplest
# technique involves shifting the letters in the message by a certain number of positions, known
# as the “shift” or “key”. Given a message and an integer shift value, print the encrypted
# message. For instance, Encryption - If shift value is 2, A becomes C, B becomes D etc. Z
# cycles back and becomes B.
# Eg1: inp_str=”Hello world” , shift_value=3, Output= Khoor zruog
# Eg2: inp_str=” Zero to hero!” , shift_value=1, Output= Afsp up ifsp!

in_str=input()
shiftkey=int(input())
out_str=""
for i in in_str:
    if i.isalpha():
        if i.isupper():
            print("loop1")
            x=(ord(i)+shiftkey)%91
            if ord(i)+shiftkey<91:
                print(x)
                print(chr(x))
                out_str+=chr(x)
            else:
                print(x+65)
                print(chr(x+65))
                out_str+=chr(x+65)
        
        else:
            x=(ord(i)+shiftkey)%123
            if ord(i)+shiftkey<123:
                print(x)
                print(chr(x))
                out_str+=chr(x)
            else:
                print(x+97)
                print(chr(x+97))
                out_str+=chr(x+97)
    else:
        out_str+=i

print(in_str,out_str,sep="\n")