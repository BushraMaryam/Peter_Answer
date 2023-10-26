from msvcrt import getch
import sys
ans=""

Question=input("Enter Question:")

print("Enter the petition:")
petition="peter please answer"
count=0
while count<len(petition):
    a=getch()
    if a.decode()!="/":
        print(a.decode(),end="")
        sys.stdout.flush()
        count=count+1
    else:
        if a.decode()=="/":
            while a.decode() =="/":
                z=getch()
                print(petition[count],end="")
                sys.stdout.flush()
                count=count+1
                if z.decode()=="/":
                    break
                else:
                    ans = ans + z.decode()

if ans=="":
      print("\nI am learning,next time when you ask the question I will surely give your answer later")
else:
      print("\n",ans)