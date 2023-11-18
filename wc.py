# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
#                         help='File to count (default: standard input)')

#     args = parser.parse_args()

#     try:
#         text = args.file.read()
#     except Exception as e:
#         print(f"Error: {e}")
#         sys.exit(1)

#     character_count = count_characters(text)
#     word_count = count_words(text)
#     line_count = count_lines(text)

#     # Print the output in the format "line_count word_count character_count"
#     print(f"{line_count}\t{word_count}\t{character_count}", end='')

#     sys.exit(0)

# if __name__ == '__main__':
#     main()

import argparse
import sys

def count_characters(text):
    return len(text.encode('utf-8'))

def count_words(text):
    words = text.split()
    return len(words)

def count_lines(text):
    return text.count('\n')

def main():
    parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='File to count (default: standard input)')

    args = parser.parse_args()

    try:
        text = args.file.read()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    character_count = count_characters(text)
    word_count = count_words(text)
    line_count = count_lines(text)

    # Print the output in the format "line_count word_count character_count filename"
    print(f"{line_count}\t{word_count}\t{character_count}", end='')

    # Print the filename if reading from a file
    if args.file.name != '<stdin>':
        print(f" {args.file.name}", end='')

    sys.stdout.flush()  # Ensure the output is flushed to stdout

    print()  # Add a newline at the end

    sys.exit(0)

if __name__ == '__main__':
    main()
