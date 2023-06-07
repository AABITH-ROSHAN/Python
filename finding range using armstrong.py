x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
for i in range(x,y+1):
    sum=0
    temp=i
    while temp>0:
        a=temp%10
        sum+=a**3
        temp//=10
        if i==sum:
            print(i)
