#initial programming 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
 
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 =int(input("What is the first number? "))
    for symbols in operations:#for user
        print(symbols)

    # operation_symbol = input("Pick the operation to be excecuted: ")
    # num2 =int(input("What is the next number? "))
    # calculation_function = operations[operation_symbol]
    # answer = calculation_function(num1, num2)
    # print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_cal = True

    while continue_cal:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
        if cont == 'y':
            num1 = answer
        
        elif cont == 'n':
            continue_cal = False
            calculator()

        else:
            print("Invalid option.")

calculator()

        

