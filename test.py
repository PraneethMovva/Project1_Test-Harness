import os
import subprocess
import re

def parse_table(output):
    lines = [line.strip() for line in output.split('\n')]

    table = [re.split(r'\s+', line) for line in lines]

    return table

def compare_tables(expected_table, actual_table):
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

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                expected_output = f.read()
                if not compare_json(expected_output.strip(), stdout.strip()):
                    return f"FAIL: {program} {test_name} failed (TestResult.OutputMismatch)\n      expected:\n{expected_output}\n\n           got:\n{stdout}"
        else:
            return f"FAIL: {program} {test_name} failed (TestResult.MissingOutputFile)"

    if os.path.exists(arg_output_file):
        with open(arg_output_file, 'r') as f:
            expected_output = f.read()
            if not compare_json(expected_output.strip(), stdout.strip()):
                return f"FAIL: {program} {test_name} failed in argument mode (TestResult.OutputMismatch)\n      expected:\n{expected_output}\n\n           got:\n{stdout}"

    return "OK"

def main():
    programs = ["gron", "wc", "ungron"]
    total_tests = 0
    failed_tests = 0

    for program in programs:
        for test_name in ["basic", "nested", "empty", "special"]:
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
