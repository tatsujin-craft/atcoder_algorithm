#!/usr/bin/env python3
"""
Script Name: auto_input_two_cards.py
Description: 
    This script runs two_cards.py with automatic input.
Usage:
    $ python3 auto_input_two_cards.py

Author: tatsujin
Date: 2024-08-17
"""


import subprocess


def run_with_auto_input(script_name, inputs):
    """
    This function runs python script with automatic input.
    """
    # Combine all inputs into a single string separated by newlines
    input_data = "\n".join(inputs)

    # Run the script with the input piped to it
    process = subprocess.Popen(
        ["python3", script_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate(input=input_data.encode())

    # Print the output from the script
    print(stdout.decode())
    if stderr:
        print(stderr.decode())


"""
入力例1
1.012
出力例1
1.012

入力例2
12.340
出力例2
12.34

入力例3
99.900
出力例3
99.9

入力例4
0.000
出力例4
0
"""


def main():
    # Define multiple input patterns
    input_patterns = [
        "1.012",
        "12.340",
        "99.900",
        "0.000",
    ]

    # Prompt the user to choose an input pattern
    print(f"Choose a gantt chart index from {list(range(1, len(input_patterns) + 1))}")
    choice = input("Enter index: ").strip()

    # Ensure the choice is valid
    if not choice.isdigit() or not 1 <= int(choice) <= len(input_patterns):
        print(
            "Invalid index. Please choose a number from "
            f"{list(range(1, len(input_patterns) + 1))}."
        )
        return

    # Convert choice to index (0-based)
    choice_index = int(choice) - 1

    # Select the input pattern based on the user's choice
    inputs = input_patterns[choice_index]

    # Name of the script to run
    script_name = "b.py"

    # Call the function to simulate input and run the script
    run_with_auto_input(script_name, [inputs])


if __name__ == "__main__":
    main()
