#Program for menu driven simple calculator
def Add(x,y):
    return x + y
def Subtract(x,y):
    return x - y
def Multiply(x,y):
    return x * y
def Divide(x,y):
    return x / y

print(" Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice=input("Enter choice(1/2/3/4): ")

    if choice in('1','2','3','4'):
        x=float(input("Enter first number"))
        y=float(input("Enter second number"))

        if choice == '1':
            print(x, "+", y, "=", Add(x,y))

        elif choice == '2':
            print(x, "-",y , "=", Subtract(x,y))

        elif choice == '3':
            print(x, "*",y , "=", Multiply(x,y))

        elif choice == '4':
            print(x, "/",y , "=", Divide(x,y))
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
