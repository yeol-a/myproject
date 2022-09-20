s=list(map(int,input().split()))
N=s[0]
M=s[1]
wood=list(map(int,input().split()))



def cuttinglevel(N, M):
    smallest=wood[0]
    for i in range(1,len(wood)-1):
        if smallest > wood[i]:
            smallest=wood[i]
    
    sum=0
    for i in range(len(wood)):
        sum+=wood[i]
    
    print(sum)
    
    target= sum - M
    print(target)
    target_list=[]
    for i in range(0, smallest+1):
        target_list.append(N*i)
        
    # print(target_list)
    start=0
    end=len(target_list)-1
    while start!=end+1:
        mid=(start+end)//2
        if target_list[mid] > target:
            end=mid-1
        else:
            start=mid+1
    if start<len(target_list) and target_list[start]==target:
        return start 
    print(start)
        
# a=cuttinglevel(N,M)
# print(a)

a=cuttinglevel(N,M)
print(a)