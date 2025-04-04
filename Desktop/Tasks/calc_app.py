import os

def perform_calculation():
    """Get user input for a calculation, perform it, and save to file."""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please use +, -, *, or /")
            return
        
        equation = f"{num1} {operation} {num2} = {result}"
        print(f"Result: {equation}")
        
        # Save to file
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")
            
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_previous_calculations():
    """Print all previous calculations from the file."""
    try:
        if not os.path.exists("equations.txt"):
            print("No previous calculations found.")
            return
            
        with open("equations.txt", "r") as file:
            equations = file.readlines()
            
        if not equations:
            print("No previous calculations found.")
        else:
            print("\nPrevious Calculations:")
            for eq in equations:
                print(eq.strip())
                
    except FileNotFoundError:
        print("No previous calculations found.")
    except Exception as e:
        print(f"An error occurred while reading calculations: {e}")

def main():
    """Main program loop."""
    while True:
        print("\nCalculator App")
        print("1. Perform Calculation")
        print("2. View Previous Calculations")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_previous_calculations()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()