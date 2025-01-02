#!/usr/bin/env python3
"""
Script Name: local_tester.py
Description: 
    This script runs Python script or C++ program with automatic input data.

Usage:
    $ ./local_tester.py <directory> <file>          # Runs the main Python script
    $ ./local_tester.py <directory> <file> --prac   # Runs the practice Python script
    $ ./local_tester.py <directory> <file> --cpp    # Compiles and runs the C++ program

Author: tatsujin
Date: 2025-01-02
"""

import subprocess
import argparse
import os
import sys


def load_input_patterns(input_data_file_path):
    """
    This function reads 2D list input data from a file
    """
    with open(input_data_file_path, "r") as file:
        content = file.read().strip()

    # Split patterns by blank lines and convert each pattern to a list of lines
    patterns = [pattern.splitlines() for pattern in content.split("\n\n")]
    return patterns


def run_with_auto_input(python_script_path, inputs):
    """
    This function runs a Python script with automatic input.
    """
    # Join the inputs with newlines
    input_data = "\n".join(inputs)

    # Run the script with the input piped to it
    process = subprocess.Popen(
        ["python3", python_script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate(input=input_data.encode())

    # Print the output from the script
    print(stdout.decode())
    if stderr:
        print(stderr.decode())


def compile_cpp(cpp_source_file_path, cpp_exe_file_path):
    """
    This function compiles the C++ source file.
    """
    compile_command = ["g++", cpp_source_file_path, "-o", cpp_exe_file_path]
    try:
        subprocess.run(compile_command, check=True)
        print(f"Build file: {cpp_exe_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed: {e}")
        sys.exit(1)


def run_cpp(cpp_exe_file_path, inputs):
    """
    This function runs the compiled C++ binary with provided inputs.
    """
    # Join the inputs with newlines
    input_data = "\n".join(inputs)

    # Run the compiled binary with the input piped to it
    process = subprocess.Popen(
        [cpp_exe_file_path],
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
    # Argument parser to handle positional and optional arguments
    parser = argparse.ArgumentParser(description="Run script with auto input")
    parser.add_argument("directory", help="Base directory for paths")
    parser.add_argument("file", help="File name to use")
    parser.add_argument("--prac", action="store_true", help="Run practice script")
    parser.add_argument("--cpp", action="store_true", help="Compile and run C++ source")
    args = parser.parse_args()

    base_dir = args.directory
    file_name = args.file

    # Define paths based on the provided directory and file name
    input_data_file_path = os.path.join(base_dir, "input_data", f"data_{file_name}.txt")
    python_script_path = os.path.join(base_dir, "scripts", f"{file_name}.py")
    python_practice_script_path = os.path.join(
        base_dir, "practice", f"prac_{file_name}.py"
    )
    cpp_source_file_path = os.path.join(base_dir, "src", f"{file_name}.cpp")
    cpp_exe_file_path = os.path.join(base_dir, "build", f"{file_name}.out")

    # Determine execution mode
    if args.cpp:
        print("Execution mode: C++")
        # Compile the C++ source file once
        compile_cpp(cpp_source_file_path, cpp_exe_file_path)
    elif args.prac:
        print("Execution mode: Python practice")
        python_script_path = python_practice_script_path
    else:
        print("Execution mode: Python")

    # Load input patterns from the file
    try:
        input_patterns = load_input_patterns(input_data_file_path)
    except FileNotFoundError:
        print(f"Input data file not found: {input_data_file_path}")
        sys.exit(1)

    # Execute each input pattern sequentially
    for index, inputs in enumerate(input_patterns, start=1):
        print(f"\n--- Execution {index} ---")

        if args.cpp:
            # Run the compiled C++ binary with each input
            run_cpp(cpp_exe_file_path, inputs)
        else:
            # Run the Python script with each input
            run_with_auto_input(python_script_path, inputs)


if __name__ == "__main__":
    main()
