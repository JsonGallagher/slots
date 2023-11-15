import random

# Set global constant value (ALL CAPS)
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Check winnings function
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Initialize winnings to zero
    winning_lines = []  # List to store the winning line numbers
    # Iterate over each line
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol from the first column in the current line
        # Check if the same symbol is present in all columns of the line
        for column in columns:
            symbol_to_check = column[line]  # Get the symbol to check from the current column
            if symbol != symbol_to_check:   # If symbols don't match, break and check the next line
                break
        else:  # This else corresponds to the for loop; it's executed if the loop wasn't broken
            winnings += values[symbol] * bet  # Calculate winnings for the line and add to total
            winning_lines.append(line + 1)  # Append the winning line number to the list
    return winnings, winning_lines  # Return the total winnings and list of winning lines

# Slot machine spin function
def get_slot_machine_spin(rows, cols, symbols):
    """
    Simulates a spin of a slot machine and returns the result as a 2D array.

    Args:
        -rows (int): The number of rows in the slot machine.
        -cols (int): The number of columns in the slot machine.
        -symbols (dict): A dictionary where keys are symbols and values are the frequency of each symbol.

    Returns:
        -list: A 2D list representing the slot machine spin outcome. Each sub-list represents a column.

    The function works by first creating a list of all symbols based on their frequency. Then, for each column, it randomly selects a symbol from this list (without replacement), ensuring that the same symbol does not appear more than once in a column if its frequency allows.
    """

    # Create a list of symbols based on their frequency.
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        # Prepare a copy of symbols for this column.
        current_symbols = all_symbols[:]

        # Randomly pick a symbol for each row in the column.
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        # Add the completed column to the list of columns.
        columns.append(column)

    return columns

#Display slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        print()

# Collect initial deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #check if is a valid whole num
            amount = int(amount)
            if amount > 0:
                break #End While loop when correct bet is entered
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please submit a valid number.")
    return amount

# Collect the bet from user, how many lines?
def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): #check if is a valid whole num
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break #End While loop when correct bet is entered
            else:
                print("Please enter a valid number of lines (1-" + str(MAX_LINES) + ")")
        else:
            print("Please enter a numerical value.")
    return lines

# Collect bet per line
def get_bet():
        while True:
            bet = input("What would you like to bet? $")
            if bet.isdigit(): #check if is a valid whole num
                bet = int(bet)
                if MIN_BET <= bet <= MAX_BET:
                    break #End While loop when correct bet is entered
                else:
                    print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
            else:
                print("Please submit a valid number.")
        return bet

def spin(balance):
    lines = get_num_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money in your balance to cover your bet. Current balance: ${balance:.2f}")
        else:
            break

    print()
    print(f"You are betting ${bet:.2f} on {lines} lines. Your total bet is ${total_bet:.2f}.\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won: ${winnings:.2f}")
    print(f"You won on line(s): ", *winning_lines)
    return winnings - total_bet

# Store into a main function so that the program can easily be re-run
def main():
    balance = deposit()

    while True:
        print(f"Current balance is: ${balance:.2f}\n")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance:.2f}")

main()