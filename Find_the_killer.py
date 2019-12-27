import random
culpritno=0
user=0

def randotron(lst):
    return random.choice(lst)

#main
lt=[1,2,3,4,5]
lst=[1,2,3,4,5]
user=int(input("Enter a number from 1-5: "))
cull=0
choice=0
temp=0
lst.pop(user-1)
lt.pop(user-1)
culpritno=randotron(lt)
lt.pop(culpritno-1)
lt.append(user)
for i in range(3,-1,-1):
    print(lst)
    choice=int(input("Enter the number you suspect: "))
    cull=randotron(lt)
    temp=cull
    if (choice==culpritno):
        print("You got the killer")
        break
    elif(choice==user):
        print("You got yourself!!! Try again")
        continue
    elif(choice>5 or choice<1):
        print("Error!!!!Try again")
        continue
    elif(cull==user):
        print("The killer( no.",culpritno,") killed you")
        break
    else:
        print("The killer killed no.",cull)
        cull=lt.index(cull)
        lt.pop(cull)
        cull=lst.index(temp)
        lst.pop(cull)
