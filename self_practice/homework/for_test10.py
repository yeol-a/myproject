for i in range(0, 10):   
    for j in range(10, i, -1):
        print(" ", end=" ")
    for k in range(0, (i+1)*2-1):
        print ("★", end= " ")
    print(" ")