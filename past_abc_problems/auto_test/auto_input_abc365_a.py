#!/usr/bin/env python3
"""
Script Name: auto_input_abc{index}_{a..g}.py
Description: 
    This script runs Python script or C++ program with automatic input data.

Usage:
    $ ./auto_input_abc{index}_{a..g}.py          # Runs the main Python script
    $ ./auto_input_abc{index}_{a..g}.py --prac   # Runs the practice Python script
    $ ./auto_input_abc{index}_{a..g}.py --cpp    # Compiles and runs the C++ program

Author: tatsujin
Date: 2024-10-13
"""

import subprocess
import argparse

# File name
FILE_NAME = "abc365_a"
# Input data file path
INPUT_DATA_FILE_PATH = f"../input_data/data_{FILE_NAME}.txt"
# Python script path
PYTHON_SCRIPT_PATH = f"../scripts/{FILE_NAME}.py"
PYTHON_PRACTICE_SCRIPT_PATH = f"../practice/prac_{FILE_NAME}.py"
# C++ file path
CPP_SOURCE_FILE_PATH = f"../src/{FILE_NAME}.cpp"
CPP_EXE_FILE_PATH = f"../build/{FILE_NAME}.out"


def load_input_patterns(file_name):
    """
    This function reads 2D list input data from a file
    """
    with open(file_name, "r") as file:
        content = file.read().strip()

    # Split patterns by blank lines and convert each pattern to a list of lines
    patterns = [pattern.splitlines() for pattern in content.split("\n\n")]
    return patterns


def run_with_auto_input(script_name, inputs):
    """
    This function runs a Python script with automatic input.
    """
    # Join the inputs with newlines
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


def compile_cpp():
    """
    This function compiles the C++ source file.
    """
    compile_command = ["g++", CPP_SOURCE_FILE_PATH, "-o", CPP_EXE_FILE_PATH]
    subprocess.run(compile_command, check=True)
    print(f"Build file: {CPP_EXE_FILE_PATH}")


def run_cpp(inputs):
    """
    This function runs the compiled C++ binary with provided inputs.
    """
    # Join the inputs with newlines
    input_data = "\n".join(inputs)

    # Run the compiled binary with the input piped to it
    process = subprocess.Popen(
        [CPP_EXE_FILE_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate(input=input_data.encode())

    # Print the output from the binary
    print(stdout.decode())
    if stderr:
        print(stderr.decode())


def main():
    # Argument parser to check for the --prac and --cpp options
    parser = argparse.ArgumentParser(description="Run script with auto input")
    parser.add_argument("--prac", action="store_true", help="Run practice script")
    parser.add_argument("--cpp", action="store_true", help="Compile and run C++ source")
    args = parser.parse_args()

    # Determine execution mode
    global PYTHON_SCRIPT_PATH
    if args.cpp:
        print("Execution mode: C++")
        # Compile the C++ source file once
        compile_cpp()
    elif args.prac:
        print("Execution mode: Python practice")
        PYTHON_SCRIPT_PATH = PYTHON_PRACTICE_SCRIPT_PATH
    else:
        print("Execution mode: Python")

    # Load input patterns from the file
    input_patterns = load_input_patterns(INPUT_DATA_FILE_PATH)

    # Execute each input pattern sequentially
    for index, inputs in enumerate(input_patterns, start=1):
        print(f"\n--- Execution {index} ---")

        if args.cpp:
            # Run the compiled C++ binary with each input
            run_cpp(inputs)
        else:
            # Call the function to simulate input and run the script
            run_with_auto_input(PYTHON_SCRIPT_PATH, inputs)


if __name__ == "__main__":
    main()
