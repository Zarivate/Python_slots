import random

# Global constant to represent certain slot machine properties
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

# Dictionary to hold all the possible symbols within a single column of the slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# Function to check whether the user has won anything from their spin
def check_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []
    # Loop through every line the user bet on, same as looping through every row that was bet on
    for line in range(lines):
        # Get the corresponding symbol from the first column in that line
        symbol = columns[0][line]
        # Loop through every column
        for column in columns:
            # Check the corresponding symbol in the following columns
            symbol_to_check = column[line]
            # If they don't match, can stop checking since no winnings and just break
            if symbol != symbol_to_check:
                break
        # Else calculate winnings
        else:
            winnings += symbol_values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Function to randomly generate the symbols that appear on each column
def get_slot_spin(rows, cols, symbols):
    # List for all the symbols
    all_symbols = []
    # For loop to get the key and value of each symbol to be added to slot. Will add each symbol however many times
    # their corresponding values are to all_symbols. IE: Will add "A" 2 times, "B" 4 times, etc.
    for symbol, symbol_count in symbols.items():
        # Anonymous variable used since just want to loop through the symbols
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Columns list that contains others lists that have all the symbols in that corresponding column
    columns = []

    # Generate an appropriate amount of symbols for every column
    for _ in range(cols):
        column = []
        # Since will have to remove values to ensure don't use more of the same symbol as what's available,
        # a copy of the list is made.
        current_symbols = all_symbols[:]
        # Select a random amount of symbols to be in the rows of the column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# Function that prints out the actual slot results
def print_slots(columns):
    # Transpose the columns matrix so the go from rows to columns, IE: The symbol columns are in rows like so
    # [A, B, C], [B, B, C], [A, C, B]. But should be instead diagonal like so
    # [A [B [C
    #  B  B  C
    #  A] C] B]

    # Nested for loop to iterate through the rows and print out the symbols in the corresponding row from each column
    for row in range(len(columns[0])):
        # Enumerate to get the index of the columns so can properly print out the pipe operator
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


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
        # If user doesn't type in a valid digit, means a number wasn't even entered so keep requesting it from them.
        else:
            print("Please enter an actual number.")

    return amount


# Function to return how many lines the user wants to bet on
def get_lines():
    while True:
        # Ask user for number of lines to bet one
        lines = input("How many lines do you wish to bet on? Goes from 1 to " + str(MAX_LINES) + ". ")
        # Make sure typed in amount is a positive whole value
        if lines.isdigit():
            # Once sure that lines is a valid whole number, convert from string to an integer
            lines = int(lines)
            # If the amount is greater than 0, can break out of loop
            if 1 <= lines <= MAX_LINES:
                break
            # Else means user entered a negative amount, keep asking for input that is positive.
            else:
                print("Please enter a number within the valid lines range.")
        # If user doesn't type in a valid digit, means a number wasn't even entered so keep requesting it from them.
        else:
            print("Please enter an actual number.")

    return lines


def get_bet():
    while True:
        # Ask user for number of lines to bet one
        bet = input("How many would you like to bet on each line? $")
        # Make sure typed in amount is a positive whole value
        if bet.isdigit():
            # Once sure that lines is a valid whole number, convert from string to an integer
            bet = int(bet)
            # If the amount is greater than 0, can break out of loop
            if MIN_BET <= bet <= MAX_BET:
                break
            # Else means user entered a negative amount, keep asking for input that is positive.
            else:
                print(f"Please enter a number within the valid range of ${MIN_BET} - ${MAX_BET}.")
        # If user doesn't type in a valid digit, means a number wasn't even entered so keep requesting it from them.
        else:
            print("Please enter an actual number.")

    return bet


def spin(balance):
    lines = get_lines()

    # User could try and be cheeky and bet more than what they can afford, keep asking them until they bet an
    # affordable amount.
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Insufficient funds to meet bet obligations. Your current balance is ${balance} against a total "
                  f"bet of ${total_bet}.")
        else:
            break
    print(f"You are currently betting ${bet} on {lines} lines. Your total bet is ${total_bet}, I wish you luck.")

    # Get the slots/columns from a simulated spin of the machine
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet)
    print(f"Your winnings are ${winnings}!")
    # Use unpack/splat operator on winning lines list to quickly and easily show the lines the user won on
    print(f"You have won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin_game = input("Press enter to spin (press q to quit). ")
        if spin_game == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
