# def linearSearch(L, target):
#     i=0
#     while L[i] != target:  #무한루프 때문에? i < len(L) ?
#         i+=1
#     if L[i] == target:
#         return i 
#     if i==len(L):
#         return -1 
#     print(i)
    

# L=[3,4,2,7,9,6]
# print(linearSearch(L, 7)) #여기가 궁금해요!


#-------------------------
# def linearSearch(L, target):
#     i=0
#     while i < len(L) and i != target:
#         i+=1
#     if i == target:
#         return i
#     else: 
#         return -1

#--------------------------
def linearSearch(L, target):
    L.append(target)
    i=0
    while L[i] != target:
        i+=1
    L.pop()
    if i==len(L):
        return -1
    
    return i # 꼭 else: return i로 안해도 되져? 

L=[3,4,2,7,9,6]
print(linearSearch(L, 7))

#--------------------------

# def linearSearch(L, target):
#     for i in range(len(L)):
#         if L[i] == target:
#             print(i)
#         if i==len(L):
#             print(-1)
            
# L=[3,4,2,7,9,6]
# linearSearch(L, 7)

#---------------------------
# def linearSearch(L, target):
#     for i in range(len(L)):
#         if L[i]==target:
#             return i
#     return -1 여기가 이해가 안가요ㅠ