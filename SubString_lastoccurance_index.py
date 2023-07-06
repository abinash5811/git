str=input()
substr=input()

for i in range(len(str)-len(substr),-1,-1):
    if str[i:i+len(substr)]==substr:
        print("last occurance of",substr,"starts at index",i)
        break