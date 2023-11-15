# Slot Machine Simulator README.md

## Overview

This Python program simulates a basic slot machine experience. It includes features such as depositing money, betting on lines, spinning the slot machine, and calculating winnings. The game is played in the console and is interactive, requiring user input for various actions such as depositing money, choosing the number of lines to bet on, and the amount to bet.

## Features

- **Deposit Functionality**: Players can deposit an amount to play.
- **Betting System**: Players choose the number of lines to bet on and the amount per line.
- **Slot Machine Simulation**: The program simulates a 3x3 slot machine with a customizable set of symbols and their values.
- **Winning Calculation**: Calculates winnings based on the symbols lined up and the bet amount.
- **Interactive Gameplay**: The game prompts the player for inputs and displays results in the console.

## How to Play

1. Run the program.
2. Deposit an initial amount of money.
3. Choose the number of lines to bet on (1 to 3).
4. Place your bet for each line.
5. The slot machine will spin, showing the outcome.
6. Winnings are calculated based on the aligned symbols.
7. Continue playing or quit the game.

## Code Structure

- **Global Constants**: Defines constants like `MAX_LINES`, `MAX_BET`, `MIN_BET`, `ROWS`, and `COLS`.
- **Symbols**: Two dictionaries, `symbol_count` and `symbol_value`, define the frequency and value of each symbol.
- **Functions**:
  - `check_winnings`: Calculates winnings based on the spin outcome.
  - `get_slot_machine_spin`: Simulates a spin of the slot machine.
  - `print_slot_machine`: Prints the slot machine's current state.
  - `deposit`: Handles the player's money deposit.
  - `get_num_of_lines`: Asks the player for the number of lines they want to bet on.
  - `get_bet`: Asks the player for their bet per line.
  - `spin`: Conducts a single spin, including betting and outcome.
  - `main`: The main game loop.

## Dependencies

- Python's `random` module.

## Installation and Running the Game

1. Ensure Python is installed on your system.
2. Save the script as `slot_machine_simulator.py`.
3. Run the script in a Python environment: `python slot_machine_simulator.py`.

## Future Enhancements

- GUI for a more immersive experience.
- Additional features like progressive jackpots or bonus games.
- More complex betting and payout rules.

## Disclaimer

This game is for entertainment purposes only and does not involve real money gambling.
