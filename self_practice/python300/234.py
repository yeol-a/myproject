def pickup_even(list):
    a=[]
    for i in range(len(list)):
        if list[i]%2==0:
            a.append(list[i])
    return a

a=[3,4,5,6,7,8]
print(pickup_even(a))
        