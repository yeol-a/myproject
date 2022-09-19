def binarySearch(L, target):
    start=0
    end=len(L)-1
    while start != end+1:
        mid=(start+end)//2
        if L[mid] > target:
            end=mid-1
        else:
            start=mid+1
    if L[start] == target and start < len(L):
        return start
    else: 
        return -1 