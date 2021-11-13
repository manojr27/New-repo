a=int(input("Enter First value:"))
b=int(input("Enter Second Value:"))
c=int(input("Enter Third Value:"))

min=a if a<b and a>b  else c

print ("A is smaller than B",min)


print("------------------")

a=int(input("Enter First value:"))
b=int(input("Enter Second Value:"))
c=int(input("Enter Third Value:"))

max=a if a<b or a>b  else c

print ("A is smaller than B",max)



print("--------------------")

a=int(input("Enter First value:"))
b=int(input("Enter Second Value:"))
c=int(input("Enter Third Value:"))

min=a if a<b and a<c else b if b<c  else c

print ("A is smaller than B",min)

print("--------------------")

a=int(input("Enter First value:"))
b=int(input("Enter Second Value:"))
c=int(input("Enter Third Value:"))

max=a if a>b and a>c else b if b>c  else c

print ("A is smaller than B",max)

print("--------------------")

a=int(input("Enter First value:"))
b=int(input("Enter Second Value:"))

print ("A is equal to B" if a==b else "a is greater than b" if a>b else "a is lesser than b")
