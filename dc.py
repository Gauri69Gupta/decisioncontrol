print(QUESTION-1)
a=int(input("Enter the year"))
if(a%4==0):
    if(a%100==0):
      if(a%400==0):
        print("It is a leap year")
      else:
        print("It is not a leap year")
else:
    print("It is not a leap year")
print("\n")
print("QUESTION-2")
a=input("Enter the length of the polygon")
b=input("Enter the breadth of the polygon")
if(a==b):
    print("It is a square")
else:
    print("It is a rectangle")
print("\n")
print("QUESTION-3")
a=input("Enter the age of first person")
b=input("Enter the age of second person")
c=input("Enter the age of third person")
if(a==b or b==c or a==c):
   if(a==b):
       print("A and B are of same age")
   elif(b==c):
      print("B and C are of same age")
   elif(a==c):
       print("A and C are of same age")
elif(a>b and a>c):
   print("A is eldest")
elif(b>a and b>c):
   print("B is eldest")
else:
   print("C is eldest")
if(a<b and a<c):
    print("A is youngest")
elif(b<a and b<c):
    print("B is youngest")
else:
    print("C is youngest")
print("\n")
print("QUESTION-4")
a=int(input("Enter the points"))
if(a>=1 and a<=50):
   print("Sorry no prize this time")
elif(a>=51 and a<=150):
   print('''WOWW!!! You won "WOODEN DOG"''')
elif(a>=151 and a<=180):
   print('''"WOWW!!! You won "BOOK"''')
elif(a>=181 and a<=200):
   print('''WOWW!!! You won "CHOCOLATE"''')
else:
   print("invalid input from user")
print("\n")
print("QUESTION-5")
a=int(input("Enter the quantity"))
cost=0
cost=a*100
if(cost>=1000):
    print("You will get discount")
    discount=0.1*cost
    total_price=cost-discount
    print("you have to pay Rs:",total_price)
else:
    print("You have not purchased worth 1000")
print("\n")


