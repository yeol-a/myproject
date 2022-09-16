for n in range(0,4):
    for i in range(4,n,-1):
        print(" ", end=" ")
    for j in range((n+1)*2-1):
        print("★", end=" ")
    print(" ")
for n in range(4, 8):
    for i in range(3,n-4,-1):
        print(" ", end=" ")
    for j in range((n-4+1)*2+1):
        print("★", end=" ")
    print(" ")