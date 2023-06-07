a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
x=0
y=0
for i in range(a,b+1):
    if(i%2==0):
        x=x+1
    else:
        y=y+1
print("Even count : ",x)
print("Odd count : ",y)
