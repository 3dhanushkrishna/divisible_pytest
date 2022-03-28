def divisible_5(a):
    if a%5==0:
        return True
    else:
        return False
def divisible_7(a):
    if a%7==0:
        return True
    else:
        return False
def divisible_9(a):
    if a%9==0:
        return True
    else:
        return False
def divisible_10(a):
    if a%10==0:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("enter the number: "))

    res=divisible_5(a)
    if res==True:
        print("it is divisible by 5")
    else:
        print("it is not divisible by 5")
    res = divisible_7(a)
    if res == True:
        print("it is divisible by 7")
    else:
        print("it is not divisible by 7")
    res=divisible_9(a)
    if res==True:
        print("it is divisible by 9")
    else:
        print("it is not divisible by 9")
    res = divisible_10(a)
    if res == True:
        print("it is divisible by 10")
    else:
        print("it is not divisible by 10")