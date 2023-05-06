# A simple program meant to emulate the functions of a slot machine.

# Function to be called when user wants to go a round on the slots
def deposit():
    while True:
        # Ask user for deposit amount
        amount = input("How much would you like to deposit? $")
        # Make sure typed in amount is a positive whole value
        if amount.isdigit():
            # Once sure that user amount is a valid whole number, convert from string to an integer
            amount = int(amount)
            # If the amount is greater than 0, can break out of loop
            if amount > 0:
                break
            # Else means user entered a negative amount, keep asking for input that is positive.
            else:
                print("Please enter a valid amount, must be greater than 0.")
        # If user doesn't type in a valid digit, means a number wasn't even entered so keep requestin it from them.
        else:
            print("Please enter an actual number.")

    return amount

def main():
    balance = deposit()
