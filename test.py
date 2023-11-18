import os
import subprocess
import json
import re

# def compare_json(expected, actual):        #getting all ok's
#     expected_parts = expected.split()
#     actual_parts = actual.split()
    
#     # Compare only the numerical parts of the output
#     return expected_parts[:3] == actual_parts[:3]
# def compare_json(expected, actual):             #Actual one
#     return expected.strip() == actual.strip()
# def compare_json(expected, actual):
#     expected_lines = expected.strip().splitlines()
#     actual_lines = actual.strip().splitlines()

#     # Compare line by line, ignoring leading/trailing whitespaces
#     for expected_line, actual_line in zip(expected_lines, actual_lines):
#         if expected_line.strip() != actual_line.strip():
#             return False

#     return True
# def compare_json(expected, actual):
#     # Split lines and remove leading/trailing whitespaces
#     expected_lines = [line.strip() for line in expected.split('\n')]
#     actual_lines = [line.strip() for line in actual.split('\n')]

#     # Compare line by line
#     return expected_lines == actual_lines
# def compare_json(expected, actual):
#     # Split lines and remove leading/trailing whitespaces
#     expected_lines = [line.strip() for line in expected.split('\n')]
#     actual_lines = [line.strip() for line in actual.split('\n')]

#     # Compare individual components (lines) of the output
#     for expected_line, actual_line in zip(expected_lines, actual_lines):
#         if expected_line != actual_line:
#             return False
#     return True
def parse_table(output):
    # Split lines and remove leading/trailing whitespaces
    lines = [line.strip() for line in output.split('\n')]

    # Parse each line as a list of values
    table = [re.split(r'\s+', line) for line in lines]

    return table

def compare_tables(expected_table, actual_table):
    # Compare tables by iterating over rows and columns
    for expected_row, actual_row in zip(expected_table, actual_table):
        if expected_row != actual_row:
            return False
    return True

def compare_json(expected, actual):
    expected_table = parse_table(expected)
    actual_table = parse_table(actual)
    return compare_tables(expected_table, actual_table)

def run_test(program, test_name):
    input_file = f"test/{program}.{test_name}.in"
    output_file = f"test/{program}.{test_name}.out"
    arg_output_file = f"test/{program}.{test_name}.arg.out"
    command = ["python", f"{program}.py", input_file]

    # Run the program with input file
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    # Check if the output matches the expected output
    if process.returncode == 0:
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                expected_output = f.read()
                if not compare_json(expected_output.strip(), stdout.strip()):
                    return f"FAIL: {program} {test_name} failed (TestResult.OutputMismatch)\n      expected:\n{expected_output}\n\n           got:\n{stdout}"
        else:
            return f"FAIL: {program} {test_name} failed (TestResult.MissingOutputFile)"

    # Check if the exit status matches the expected exit status
    if os.path.exists(arg_output_file):
        with open(arg_output_file, 'r') as f:
            expected_output = f.read()
            if not compare_json(expected_output.strip(), stdout.strip()):
                return f"FAIL: {program} {test_name} failed in argument mode (TestResult.OutputMismatch)\n      expected:\n{expected_output}\n\n           got:\n{stdout}"

    return "OK"
# def run_test(program, test_name):
#     input_file = f"test/{program}.{test_name}.in"
#     output_file = f"test/{program}.{test_name}.out"
#     arg_output_file = f"test/{program}.{test_name}.arg.out"
#     command = ["python", f"{program}.py", input_file]

#     # Run the program with input file
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     stdout, stderr = process.communicate()

#     # Check if the output matches the expected output
#     if process.returncode == 0:
#         if os.path.exists(output_file):
#             with open(output_file, 'r') as f:
#                 expected_output = f.read()
#                 if not compare_json(expected_output.strip(), stdout.strip()):
#                     print(f"DEBUG: expected={expected_output.strip()}")
#                     print(f"DEBUG: actual={stdout.strip()}")
#                     return f"FAIL: {program} {test_name} failed (TestResult.OutputMismatch)\n      expected:\n{expected_output}\n\n           got:\n{stdout}"
#         else:
#             return f"FAIL: {program} {test_name} failed (TestResult.MissingOutputFile)"

#     # Check if the exit status matches the expected exit status
#     if os.path.exists(arg_output_file):
#         with open(arg_output_file, 'r') as f:
#             expected_output = f.read()
#             expected_output_parts = expected_output.strip().split()
#             actual_output_parts = stdout.strip().split()
#             if expected_output_parts[:3] != actual_output_parts[:3]:
#                 print(f"DEBUG: expected={expected_output.strip()}")
#                 print(f"DEBUG: actual={stdout.strip()}")
#                 return f"FAIL: {program} {test_name} failed in argument mode (TestResult.OutputMismatch)\n      expected:\n{expected_output}\n\n           got:\n{stdout}"

#     return "OK"

def main():
    programs = ["gron", "wc"]  # Add more programs as needed
    total_tests = 0
    failed_tests = 0

    for program in programs:
        for test_name in ["basic", "nested", "empty", "notfound", "special", "err"]:  # Add more test names as needed
            total_tests += 1
            result = run_test(program, test_name)
            print(result)

            if result.startswith("FAIL"):
                failed_tests += 1

    print(f"\nOK: {total_tests - failed_tests}")
    print(f"output mismatch: {failed_tests}")
    print(f"total: {total_tests}")

    if failed_tests > 0:
        exit(1)

if __name__ == "__main__":
    main()
