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

A, B = map(int, input().split())
C = int(input())

if 60*A+B+C >= 1440:
    H = abs(C-(60-B)) // 60
    M = abs(C-(60-B)) % 60
    print(H, M)
else: 
    H = (60*A+B+C) // 60
    M = (60*A+B+C) % 60
    print(H, M)
    




