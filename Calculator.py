# Simple Calculator

def calculator():
    while True:
        print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")
        choice = input("Enter choice: ")

        if choice == '5':
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", a + b)
        elif choice == '2':
            print("Result:", a - b)
        elif choice == '3':
            print("Result:", a * b)
        elif choice == '4':
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", a / b)

calculator()
