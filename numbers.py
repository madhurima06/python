no1=int(input("enter no1"))
no2=int(input("enter no2"))
no3=int(input("enter no3"))
if(no1>no2) and (no1>no3):
    bigger=no1
elif(no2>no1) and (no2>no3):
    bigger=no2
else:
    bigger=no3
    print("bigger no is:",bigger)
