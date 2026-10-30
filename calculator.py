def calculator():
    print("\n==== SMART CALCULATOR ====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division(/)")
    print("5. Remainder(%)")
    print("6. Power(**)")
    print("7. Exit")

    while True:
        choice  = input("\nChoose an operation you want to perform(1-7): ")


        if choice == "7":
            print("Calculator closed.Goodbye!")
            break

        if choice not in ["1","2","3","4","5","6"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the Second number: "))
        except ValueError:
            print("Invalid input! PLease enter number only.")
            continue
        if choice == "1":
            result = num1 +  num2

        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result  =  num1 * num2

        elif choice == "4":
            if num2 ==0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2

        elif choice == "5":
            # if num1 ==0 and num2 ==0:
            #     print("Error")
            #     continue
            if num2 == 0:
                print("Error")
                continue
            result = num1 % num2

        elif choice == "6":
            result = num1 ** num2

        print("Result:", result)

if __name__ == "__main__":
    calculator()

calculator()