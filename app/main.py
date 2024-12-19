def validate_input(prompt, input_type=float, min_value=None):
    """
    Validates user input.
    - prompt: The message displayed to the user.
    - input_type: The expected data type (default is float).
    - min_value: The minimum allowed value (default is None).
    """
    while True:
        try:
            value = input_type(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Error: The value must be greater than or equal to {min_value}.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def calculate_net(brutto, tax_rate):
    """
    Calculates net amount from gross using the formula: 
    Net = Gross / (1 + Tax Rate / 100).
    (od sta)
    """
    return brutto / (1 + tax_rate / 100)


def calculate_brutto(netto, tax_rate):
    """
    Calculates gross amount from net using the formula: 
    Gross = Net * (1 + Tax Rate / 100).
    (w stu)
    """
    return netto * (1 + tax_rate / 100)


def user_interface():
    """
    User interface for selecting the type of calculation.
    - Allows users to choose between calculating net from gross or gross from net.
    - Handles user inputs and provides results based on the selected calculation.
    """
    print("Welcome to the gross-net calculator!")
    print("1. Calculate net from gross")
    print("2. Calculate gross from net")
    
    # Validate user's choice
    choice = validate_input("Select an option (1 or 2): ", int, 1)
    
    if choice == 1:
        # Handle calculation for net from gross
        brutto = validate_input("Enter gross amount: ", float, 0.01)
        tax_rate = validate_input("Enter VAT rate (%): ", float, 0.01)
        netto = calculate_net(brutto, tax_rate)
        print(f"Net amount: {netto:.2f} zł")
    elif choice == 2:
        # Handle calculation for gross from net
        netto = validate_input("Enter net amount: ", float, 0.01)
        tax_rate = validate_input("Enter VAT rate (%): ", float, 0.01)
        brutto = calculate_brutto(netto, tax_rate)
        print(f"Gross amount: {brutto:.2f} zł")
    else:
        print("Invalid selection. Please try again.")


if __name__ == "__main__":
    user_interface()
