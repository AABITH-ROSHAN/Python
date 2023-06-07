a=int(input("Enter the birth date:"))
b=int(input("Enter the current year:"))
z=b-a
if(z>=60):
  x=1020*(20/100)
  y=1020-x
  print("the omni bus charge:",y)
else:
  print("The omni bus charge is 1020")
