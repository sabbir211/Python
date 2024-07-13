print("__________Mini Calculator For Fancy Calculation_________________")
print()
print()

a=int(input("Enter a number:"))
operator=input("what you want to do(+,-,*,/)")
b=int(input("Enter second number:"))

if operator=="+" :
    print("Sum=",(a+b))
elif(operator=="-"):
    print("Subtracts=",(a-b))
elif(operator=="*"):
    print("Multiplication=",(a*b))
elif(operator=="/"):
    print("Division=",(a/b))

else: print("Enter valid input")
print()
print()


