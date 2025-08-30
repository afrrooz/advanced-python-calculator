import operations  as op
import history
def menu():
    print("\n=== Python Advanced Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Factorial")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. View History")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an operation: ")

        if choice == "0":
            print("Exiting calculator.... goodbye!.")
            break
        elif choice in ["1","2","3","4"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input, Enter numbers only.")
                continue

            if choice =="1":
                result = op.add(a,b); expr = f"{a} + {b}"

            elif choice =="2":
                result = op.subtract(a,b); expr = f"{a} - {b}"

            elif choice =="3":
                result = op.multiply(a,b); expr = f"{a} * {b}"

            elif choice =="4":
                result = op.divide(a,b); expr = f"{a} / {b}"

        elif choice in ["5","6","7","8","9"]:
            try:
                a = float(input("Enter a number:"))
            except ValueError:
                print("Invalid input, please enter a number:")
                continue
            if choice =="5":
                result = op.squareroot(a); expr= f"squareroot{a}"
            elif choice =="6":
                result = op.factorial(int(a)); expr= f"{int(a)}!"
            elif choice =="7":
                result = op.sine(a); expr= f"sin{a}"
            elif choice =="8":
                result = op.cosine(a); expr= f"cos{a}"
            elif choice =="9":
                result = op.tangent(a); expr= f"tan{a}"
        elif choice == "10":
            print("\n---- Calculation History ----")
            print(history.view_history())
            continue
        else:
            print("Invalid option. please try again.")
            continue
        
        print(f"Result: {result}")
        history.save_history(expr, result)
            
            
if __name__ == "__main__":
    main()
