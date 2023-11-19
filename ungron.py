import re
import argparse
import sys
import json

def ungron(input_lines):
    json_dict = {}
    current_dict = json_dict
    stack = []

    for line in input_lines:
        match = re.match(r'^(\s*)(.+?) = (.+?);$', line)
        if match:
            spaces, key, value = match.groups()
            key_parts = key.split('.')
            key_parts[-1] = key_parts[-1].replace('[', '.').replace(']', '')
            
            current_dict = json_dict
            for part in key_parts[:-1]:
                current_dict = current_dict.setdefault(part, {})
            current_dict[key_parts[-1]] = json.loads(value)
        elif line.startswith('};'):
            stack.pop()
            current_dict = stack[-1]

    return json.dumps(json_dict, indent=2)

def main():
    parser = argparse.ArgumentParser(description='JSON unformatter utility (ungron) in Python')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='File to unformat (default: standard input)')

    args = parser.parse_args()
    input_lines = args.file.readlines()
    output_json = ungron(input_lines)

    print(output_json)

if __name__ == '__main__':
    main()
