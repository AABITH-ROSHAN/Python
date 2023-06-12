import math
number=int(input("Enter th number:"))
root=math.sqrt(number)
if int(root)**2==number:
    print("It is a perfect square")
else:
    print("It is not a perfect square")
