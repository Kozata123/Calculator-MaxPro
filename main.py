from models import Calculator

def run_app():
    calc = Calculator()
    
    print(f"=== Welcome to {calc.name} ===")
    
    while True:
        print("Available Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Exit")
        
        choice = input("\nChoose an option (1-7): ").strip()
        
        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice != ['1', '2', '3', '4', '5', '6']:
            print("Invalid selection. Please try again.")
            continue
            
        
        try:
            if choice == '6':
                num = float(input("Enter number: "))
                result = calc.square_root(num)
                print(f"\n-> Result: √{num} = {result}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                print("-" * 30)
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {calc.add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {calc.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {calc.multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {calc.divide(num1, num2)}")
                elif choice == '5':
                    print(f"Result: {num1} ^ {num2} = {calc.power(num1, num2)}")
                print("-" * 30)
                
        except ValueError:
            print("\nError: Please enter valid numbers only.")

if __name__ == "__main__":
    run_app()
