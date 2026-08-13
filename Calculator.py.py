a =float(input("ENTER THE FIRST NUMBER :"))
b= float(input("ENTER THE SOCOND NUMBER :"))

# AARITHMETIC OPERATORS

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. modulus")

choice= input("enter your choice from 1/2/3/4/5 :")

if choice== "1":
    print("result is =",a+b)
elif choice== "2":
    print("result is =", a-b)

elif choice== "5":
    print("result is =", a%b)


elif choice== "3":
    print("result is =", a*b)
elif choice =="4":
   if b!=0:
     print("result is=", a/b)
   else:
     print("CHUTIYA HAI KYA BE ZERO SE DIVIDE KR RHA HAI")
  

    
name= input ("ENTER YOUR NAME :")
print("THANKS FOR CHOOSING US :",name)


    
