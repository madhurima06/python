n1=int(input("enter n1"))
n2=int(input("enter n2"))
n3=int(input("enter n3"))
def bigger_no(n1,n2,n3):
    if(n1>n2) and (n1>n3):
      bigger_no=n1
    elif (n2>n1) and (n2>n3):
      bigger_no=n2
    else:
        bigger_no=n3
    return bigger_no
print(bigger_no(n1,n2,n3))
      

    
