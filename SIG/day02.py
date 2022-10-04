'''
N = int(input())
A = list(map(int, input().split()))
print(min(A), max(A))
'''
# a = [1,2,3,4]5

# print(max(a), min(a))

'''
def solve(a:list) -> int:
    return sum(a)
''' 

# def selfnum(n):
#     while 
#     n = n + str(n[0]) + str(n[1])
    

# S = input().lower
# alphabet = range(a, z)
# S.index(alphabet)
'''
inp = int(input())
a = []
for i in range(inp):
    a.append(int(input()))
a = sorted(a)
for i in range(len(a)):
    print(a[i])
'''

def recursion(S, l, r):
    if l >= r:
        return 1
    elif S[l] != S[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(S):
    return recursion(S, 0, len(S)-1)