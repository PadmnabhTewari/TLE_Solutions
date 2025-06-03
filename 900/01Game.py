for i in range(int(input())):
    a=input()
    z=a.count('0')
    z=min(z,len(a)-z)
    if(z%2!=0):
        print("DA")
    else:
        print("NET")
