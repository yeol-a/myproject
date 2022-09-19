import random

    
cycle=1
win=0
fail=0
same=0

while cycle<11:
    me=random.randint(0,2)
    you=input("가위,바위,보: ")
    if you=="바위":
        you=0
    elif you=="가위":
        you=1
    elif you=="보":
        you=2
    else:
        you=10
        
    if you==me:
        print("비겼다")
        same+=1
    elif you-me==-1 or (you==2 and me==0):
        print("이겼습니다.")
        win+=1
    elif you-me==1 or (you==0 and me==2):
        print("졌습니다.")
        fail+=1
    else:
        print("잘못내셨습니다")
        fail+=1
        
    cycle+=1

    
print("\n승:{}\n패:{}\n비김:{}".format(win, fail, same))