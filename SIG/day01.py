# inp=input()
# inp= inp.split()
# a = int(inp[0])
# b = int(inp[1])
# print(a+b)


# a, b=map(int, input().split())
# print(a+b)

# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# id=input()
# print(id+"??!")

# year=int(input()) - 543
# print(year)

# a, b, c, d, e, f= map(int, input().split())
# print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)
'''
a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)
'''

# a = input()
# b = input()
# print(int(a)*int(b[2]))
# print(int(a)*int(b[1]))
# print(int(a)*int(b[0]))
# print(int(a)*int(b))

# A, B = map(int, input().split())
# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# else:
#     print("==")

# score = int(input())
# if 90 <= score <=100:
#     print("A")
# elif 80 <= score <=89:
#     print("B")
# elif 70 <= score <=79:
#     print("C")
# elif 60 <= score <=69:
#     print("D")
# else:
#     print("F")

#꼭 elif 로 해야하는지? 

# year=int(input())
# if year % 4 == 0 and year % 100 !== 0:

# T = int(input())
# for i in range(T+1):
#     A, B = map(int, input().split())
#     print(f"Case #{i}: {A+B}")

# class AyoungKim(object):
# 	def __init__(self, effort):
# 		self.effort=effort
# 	def __call__(self):
# 		if self.effort:
# 			print("success") 
# 		else:
# 			print("suicide")

# ay = AyoungKim(3)
# ay()


#print("\    /\ \n )  ( ')\n(  /  )\n \(__)|")


#print("|\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\__|")

# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`   

# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\\/")
# print("      |")
# print("      |")

# year = int(input())
# if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
#     print(1)
# else:
#     print(0)




# x=int(input()) 
# y=int(input())

# if x > 0 and y > 0 :
#     print(1)
# elif x < 0 and y > 0 :
#     print(2)
# elif x < 0 and y < 0 :
#     print(3)
# else:
#     print(4)



# if H >= 0 and M >= 45:
#     print(H, M-45)
# elif H > 0 and M < 45:
#     print(H-1, 60+M-45)
# elif H == 0 and M < 45:
#     print(23, 60+M-45)
    
# H, M = map(int, input().split())
# if   < 45:
#     print(23, 60-(45-M))
# else:
#     H = (60*H+M-45)//60
#     M = (60*H+M-45)%60
#     print(H, M)


'''
A, B = map(int, input().split())
C = int(input())

m = 60 * A + B + C
if m >= 1440:
    m -= 1440
    
H = m // 60
M = m % 60

print(H, M)
'''

'''
A, B, C = map(int, input().split())

if A==B==C:
    print(10000+A*1000)
elif A==B:
    print(1000+A*100)
elif A==C:
    print(1000+A*100)
elif B==C:
    print(1000+B*100)
else:
    print(100*max(A, B, C))
'''
'''
inp = int(input())

for i in range(1,10):
    print(inp, "*", i, "=", inp*i)
'''
'''
test = int(input())
for i in range(test):
    A, B = map(int, input().split())
    print(A+B)
'''
'''
inp = int(input())
sum = 0

for i in range(1, inp+1):
    sum += i 
print(sum)
'''
'''
X = int(input())
N = int(input())
sum = 0

for i in range(1, N+1):
    a, b = map(int, input().split())
    sum += a*b
if sum == X:
    print("Yes")
else:
    print("No")
'''


'''
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)
'''
'''
import sys 
T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
'''
'''
import sys
T = int(input())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    sum = A + B
    print(f"Case #{i}: {sum}")
'''
'''
import sys
T = int(input())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")
'''

'''
N = int(input())
for i in range(1, N+1):
    print(" "*(N-i)+"*"*i)
'''
'''
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(len(A)):
    if A[i] < X:
        print(A[i], end=" ")
'''
'''
A, B = map(int, input().split())
print(A+B)
while (A, B) != (0, 0): 
    A, B = map(int, input().split())
    print(A+B)
'''
'''
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
'''
'''
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
        '''




n = input()
num = n
cnt = 0

while True:
    if len(num) == 1:
        num = "0" + num
    plus = str(int(num[0])+int(num[1]))
    num = num[-1]+plus[-1]
    cnt +=1
    if num == n:
        print(cnt)
        break 
    
n = int(input())
num = n
cnt = 0

while 1:
    