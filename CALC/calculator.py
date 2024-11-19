# Simple Calculator Application

def calculator():
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    result = num1 + num2
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == "2":
                    result = num1 - num2
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == "3":
                    result = num1 * num2
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == "4":
                    if num2 != 0:
                        result = num1 / num2
                        print(f"Result: {num1} / {num2} = {result}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        elif choice == "5":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    calculator()
