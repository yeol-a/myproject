def binarySearch(L, target):
    start=0
    end=len(L)-1
    mid=(start+end)//2
    while L[mid] != target:
        if L[mid] > target:
            end=mid-1
        else:
            start=mid+1
        mid=(start+end)//2
    if L[mid] == target:
        return mid
    else:
        return -1


L=[1,3,5,6,8,9]
a = binarySearch(L, 10)
print(a)
