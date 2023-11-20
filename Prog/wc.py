import argparse
import sys

def count_characters(text):
    return len(text.encode('utf-8'))

def count_words(text):
    words = text.split()
    return len(words)

def count_lines(text):
    return text.count('\n')

def count_occurrences(text, word):
    return text.split().count(word)

def process_file(file_path, occurrences_word):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            character_count = count_characters(text)
            word_count = count_words(text)
            line_count = count_lines(text)
            occurrences_count = count_occurrences(text, occurrences_word) if occurrences_word else 0
            return line_count, word_count, character_count, occurrences_count
    except Exception as e:
        return f"Error: {e}"

def main():
    parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
    parser.add_argument('files', nargs='*', type=str, help='Files to count')
    parser.add_argument('-l', '--lines', action='store_true', help='Count only lines')
    parser.add_argument('-w', '--words', action='store_true', help='Count only words')
    parser.add_argument('-c', '--characters', action='store_true', help='Count only characters')
    parser.add_argument('-occurrences', type=str, help='Count occurrences of a specific word')

    args = parser.parse_args()

    if args.lines and args.occurrences:
        if args.files:
            total_occurrences = 0
            total_lines = 0
            total_words = 0
            total_characters = 0
            for file_path in args.files:
                result = process_file(file_path, args.occurrences)
                if isinstance(result, tuple):
                    lines, words, characters, occurrences = result
                    total_occurrences += occurrences
                    total_lines += lines
                    total_words += words
                    total_characters += characters
                    print(f"Occurrences of {args.occurrences} in {file_path}: {occurrences}")
                else:
                    print(result)
            print(f"Occurrences of {args.occurrences} in total: {total_occurrences}")
            print(f"{total_lines}\t{total_words}\t{total_characters} total")
            sys.exit(0)
        else:
            print(f"Error: -l and -occurrences cannot be used together.")
            sys.exit(1)

    if not args.files:
        print("Error: At least one file must be specified.")
        sys.exit(1)

    total_lines, total_words, total_characters, total_occurrences = 0, 0, 0, 0

    for file_path in args.files:
        result = process_file(file_path, args.occurrences)

        if isinstance(result, tuple):
            lines, words, characters, occurrences = result
            total_lines += lines
            total_words += words
            total_characters += characters
            total_occurrences += occurrences

            if not args.lines and not args.words and not args.characters:
                if args.occurrences:
                    print(f"Occurrences of {args.occurrences} in {file_path}: {occurrences}")
                print(f"{lines}\t{words}\t{characters} {file_path}")
            else:
                output = ''
                if args.lines:
                    output += f"{lines} "
                if args.words:
                    output += f"{words} "
                if args.characters:
                    output += f"{characters} "
                if args.occurrences:
                    output += f"{occurrences} "
                print(output.strip(), file_path)
        else:
            print(result)

    if len(args.files) > 1:
        if not args.lines and not args.words and not args.characters:
            if args.occurrences:
                print(f"Occurrences of {args.occurrences} in total: {total_occurrences}")
            print(f"{total_lines}\t{total_words}\t{total_characters} total")
        else:
            output = ''
            if args.lines:
                output += f"{total_lines} "
            if args.words:
                output += f"{total_words} "
            if args.characters:
                output += f"{total_characters} "
            if args.occurrences:
                output += f"{total_occurrences} "
            print(output.strip(), "total")

if __name__ == '__main__':
    main()

