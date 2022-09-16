line=int(input())
#print(" "*3, "★", " "*3)
for n in range(1,line):
    if (n-1)%4==0:
        n=(n-1)//4+1
    if (n-1)%4==1:
        n=(n-1)//4+2
    if (n-1)%4==2:
        n=(n-1)//4+3 
    if (n-1)%4==3:
        n=n??   
    print(" "*(3-n),"★"*(2*n-1)," "*(3-n))
    