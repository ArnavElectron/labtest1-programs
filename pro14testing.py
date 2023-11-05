in_str=input()
shiftkey=int(input())
out_str=""
for i in in_str:
    print("i",i)
    print("asci i ",ord(i))
    print("asci i +sk",ord(i)+shiftkey)
    print("asci i +sk%122",(ord(i)+shiftkey)%122)
    print("asci i +sk%122+96",((ord(i)+shiftkey)%122)+96)
    print("chr asci i +sk%122+96",chr(((ord(i)+shiftkey)%122)+96))