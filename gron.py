import json
import argparse
import sys

def format_output(obj_name, key, value):
    if isinstance(value, dict):
        print(f"{key} = {{}};")
        for sub_key, sub_value in value.items():
            format_output(obj_name, f"{key}.{sub_key}", sub_value)
    elif isinstance(value, list):
        print(f"{key} = [];")
        for i, item in enumerate(value):
            format_output(obj_name, f"{key}[{i}]", item)
    else:
        print(f"{key} = {json.dumps(value)};")

def gron(json_data, obj_name='json'):
    try:
        parsed_json = json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Error: Unable to parse JSON - {e}")
        sys.exit(1)

    format_output(obj_name, obj_name, parsed_json)

def main():
    parser = argparse.ArgumentParser(description='JSON formatter utility (gron) in Python')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='File to format (default: standard input)')
    parser.add_argument('--obj', type=str, default='json', help='Specify a different base object name')

    args = parser.parse_args()

    json_data = args.file.read()
    gron(json_data, args.obj)

    sys.exit(0)

if __name__ == '__main__':
    main()

















#Two .. printing
# import json
# import argparse
# import sys

# def format_output(obj_name, key, value):
#     if isinstance(value, dict):
#         print(f"{obj_name}.{key} = {{}};")
#         for sub_key, sub_value in value.items():
#             format_output(f"{obj_name}.{key}", sub_key, sub_value)
#     elif isinstance(value, list):
#         print(f"{obj_name}.{key} = [];")
#         for i, item in enumerate(value):
#             format_output(f"{obj_name}.{key}", f"{i}", item)
#     else:
#         print(f"{obj_name}.{key} = {json.dumps(value)};")

# def gron(json_data, obj_name='json'):
#     try:
#         parsed_json = json.loads(json_data)
#     except json.JSONDecodeError as e:
#         print(f"Error: Unable to parse JSON - {e}")
#         sys.exit(1)

#     format_output(obj_name, '', parsed_json)

# def main():
#     parser = argparse.ArgumentParser(description='JSON formatter utility (gron) in Python')
#     parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
#                         help='File to format (default: standard input)')
#     parser.add_argument('--obj', type=str, default='json', help='Specify a different base object name')

#     args = parser.parse_args()

#     json_data = args.file.read()
#     gron(json_data, args.obj)

#     sys.exit(0)

# if __name__ == '__main__':
#     main()






#Normal one
# import json
# import argparse
# import sys

# def format_output(key, value):
#     if isinstance(value, dict):
#         print(f"{key} = {{}};")
#         for sub_key, sub_value in value.items():
#             format_output(f"{key}.{sub_key}", sub_value)
#     elif isinstance(value, list):
#         print(f"{key} = [];")
#         for i, item in enumerate(value):
#             format_output(f"{key}[{i}]", item)
#     else:
#         print(f"{key} = {json.dumps(value)};")

# def gron(json_data):
#     try:
#         parsed_json = json.loads(json_data)
#     except json.JSONDecodeError as e:
#         print(f"Error: Unable to parse JSON - {e}")
#         sys.exit(1)

#     format_output('json', parsed_json)

# def main():
#     parser = argparse.ArgumentParser(description='JSON formatter utility (gron) in Python')
#     parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
#                         help='File to format (default: standard input)')

#     args = parser.parse_args()

#     json_data = args.file.read()
#     gron(json_data)

#     sys.exit(0)

# if __name__ == '__main__':
#     main()
