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




#SO far Best
# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def count_occurrences(text, word):
#     return text.split().count(word)

# def process_file(file_path, occurrences_word):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             character_count = count_characters(text)
#             word_count = count_words(text)
#             line_count = count_lines(text)
#             occurrences_count = count_occurrences(text, occurrences_word) if occurrences_word else 0
#             return line_count, word_count, character_count, occurrences_count
#     except Exception as e:
#         return f"Error: {e}"

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('files', nargs='*', type=str, help='Files to count')
#     parser.add_argument('-l', '--lines', action='store_true', help='Count only lines')
#     parser.add_argument('-w', '--words', action='store_true', help='Count only words')
#     parser.add_argument('-c', '--characters', action='store_true', help='Count only characters')
#     parser.add_argument('-occurrences', type=str, help='Count occurrences of a specific word')

#     args = parser.parse_args()

#     if args.lines and args.occurrences:
#         if args.files:
#             total_occurrences = 0
#             total_lines = 0
#             total_words = 0
#             total_characters = 0
#             for file_path in args.files:
#                 result = process_file(file_path, args.occurrences)
#                 if isinstance(result, tuple):
#                     lines, words, characters, occurrences = result
#                     total_occurrences += occurrences
#                     total_lines += lines
#                     total_words += words
#                     total_characters += characters
#                     print(f"Occurrences of {args.occurrences} in {file_path}: {occurrences}")
#                 else:
#                     print(result)
#             print(f"Occurrences of {args.occurrences} in total: {total_occurrences}")
#             print(f"{total_lines}\t{total_words}\t{total_characters} total")
#             sys.exit(0)
#         else:
#             print(f"Error: -l and -occurrences cannot be used together.")
#             sys.exit(1)

#     if not args.files:
#         print("Error: At least one file must be specified.")
#         sys.exit(1)

#     total_lines, total_words, total_characters, total_occurrences = 0, 0, 0, 0

#     for file_path in args.files:
#         result = process_file(file_path, args.occurrences)

#         if isinstance(result, tuple):
#             lines, words, characters, occurrences = result
#             total_lines += lines
#             total_words += words
#             total_characters += characters
#             total_occurrences += occurrences

#             if not args.lines and not args.words and not args.characters:
#                 if args.occurrences:
#                     print(f"Occurrences of {args.occurrences} in {file_path}: {occurrences}")
#                 print(f"{lines}\t{words}\t{characters} {file_path}")
#             else:
#                 output = ''
#                 if args.lines:
#                     output += f"{lines} "
#                 if args.words:
#                     output += f"{words} "
#                 if args.characters:
#                     output += f"{characters} "
#                 if args.occurrences:
#                     output += f"{occurrences} "
#                 print(output.strip(), file_path)
#         else:
#             print(result)

#     if len(args.files) > 1:
#         if not args.lines and not args.words and not args.characters:
#             if args.occurrences:
#                 print(f"Occurrences of {args.occurrences} in total: {total_occurrences}")
#             print(f"{total_lines}\t{total_words}\t{total_characters} total")
#         else:
#             output = ''
#             if args.lines:
#                 output += f"{total_lines} "
#             if args.words:
#                 output += f"{total_words} "
#             if args.characters:
#                 output += f"{total_characters} "
#             if args.occurrences:
#                 output += f"{total_occurrences} "
#             print(output.strip(), "total")

# if __name__ == '__main__':
#     main()






#OK
# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def count_occurrences(text, word):
#     return text.split().count(word)

# def process_file(file_path, occurrences_word):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             character_count = count_characters(text)
#             word_count = count_words(text)
#             line_count = count_lines(text)
#             occurrences_count = count_occurrences(text, occurrences_word) if occurrences_word else 0
#             return line_count, word_count, character_count, occurrences_count
#     except Exception as e:
#         return f"Error: {e}"

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('files', nargs='*', type=str, help='Files to count')
#     parser.add_argument('-l', '--lines', action='store_true', help='Count only lines')
#     parser.add_argument('-w', '--words', action='store_true', help='Count only words')
#     parser.add_argument('-c', '--characters', action='store_true', help='Count only characters')
#     parser.add_argument('-occurrences', type=str, help='Count occurrences of a specific word')

#     args = parser.parse_args()

#     if args.lines and args.occurrences:
#         if args.files:
#             total_occurrences = 0
#             for file_path in args.files:
#                 result = process_file(file_path, args.occurrences)
#                 if isinstance(result, tuple):
#                     occurrences = result[-1]
#                     total_occurrences += occurrences
#                     print(f"Occurrences of {args.occurrences} in {file_path}: {occurrences}")
#                 else:
#                     print(result)
#             print(f"Occurrences of {args.occurrences} in total: {total_occurrences}")
#             sys.exit(0)
#         else:
#             print(f"Error: -l and -occurrences cannot be used together.")
#             sys.exit(1)

#     if not args.files:
#         print("Error: At least one file must be specified.")
#         sys.exit(1)

#     total_lines, total_words, total_characters, total_occurrences = 0, 0, 0, 0

#     for file_path in args.files:
#         result = process_file(file_path, args.occurrences)

#         if isinstance(result, tuple):
#             lines, words, characters, occurrences = result
#             total_lines += lines
#             total_words += words
#             total_characters += characters
#             total_occurrences += occurrences

#             if not args.lines and not args.words and not args.characters:
#                 if args.occurrences:
#                     print(f"Occurrences of {args.occurrences} in {file_path}: {occurrences}")
#                 print(f"{lines}\t{words}\t{characters}\t{occurrences} {file_path}")
#             else:
#                 output = ''
#                 if args.lines:
#                     output += f"{lines} "
#                 if args.words:
#                     output += f"{words} "
#                 if args.characters:
#                     output += f"{characters} "
#                 if args.occurrences:
#                     output += f"{occurrences} "
#                 print(output.strip(), file_path)
#         else:
#             print(result)

#     if len(args.files) > 1:
#         if not args.lines and not args.words and not args.characters:
#             if args.occurrences:
#                 print(f"Occurrences of {args.occurrences} in total: {total_occurrences}")
#             print(f"{total_lines}\t{total_words}\t{total_characters}\t{total_occurrences} total")
#         else:
#             output = ''
#             if args.lines:
#                 output += f"{total_lines} "
#             if args.words:
#                 output += f"{total_words} "
#             if args.characters:
#                 output += f"{total_characters} "
#             if args.occurrences:
#                 output += f"{total_occurrences} "
#             print(output.strip(), "total")

# if __name__ == '__main__':
#     main()




#Cool but can be improved
# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def count_occurrences(text, word):
#     return text.split().count(word)

# def process_file(file_path, occurrences_word=None):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             character_count = count_characters(text)
#             word_count = count_words(text)
#             line_count = count_lines(text)
#             occurrences_count = count_occurrences(text, occurrences_word) if occurrences_word else 0
#             return line_count, word_count, character_count, occurrences_count
#     except Exception as e:
#         return f"Error: {e}"

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('files', nargs='*', type=str, help='Files to count')
#     parser.add_argument('-l', '--lines', action='store_true', help='Count only lines')
#     parser.add_argument('-w', '--words', action='store_true', help='Count only words')
#     parser.add_argument('-c', '--characters', action='store_true', help='Count only characters')
#     parser.add_argument('-occurrences', type=str, help='Count occurrences of a specific word')

#     args = parser.parse_args()

#     if args.lines and args.occurrences:
#         print("Error: -l and -occurrences cannot be used together.")
#         sys.exit(1)

#     if not args.files:
#         print("Error: At least one file must be specified.")
#         sys.exit(1)

#     total_lines, total_words, total_characters, total_occurrences = 0, 0, 0, 0

#     for file_path in args.files:
#         result = process_file(file_path, args.occurrences)

#         if isinstance(result, tuple):
#             lines, words, characters, occurrences = result
#             total_lines += lines
#             total_words += words
#             total_characters += characters
#             total_occurrences += occurrences

#             if not args.lines and not args.words and not args.characters:
#                 if args.occurrences:
#                     print(f"Occurrences of {args.occurrences} in {file_path}: {occurrences}")
#                 print(f"{lines}\t{words}\t{characters}\t{occurrences} {file_path}")
#             else:
#                 output = ''
#                 if args.lines:
#                     output += f"{lines} "
#                 if args.words:
#                     output += f"{words} "
#                 if args.characters:
#                     output += f"{characters} "
#                 if args.occurrences:
#                     output += f"{occurrences} "
#                 print(output.strip(), file_path)
#         else:
#             print(result)

#     if len(args.files) > 1:
#         if not args.lines and not args.words and not args.characters:
#             if args.occurrences:
#                 print(f"Occurrences of {args.occurrences} in total: {total_occurrences}")
#             print(f"{total_lines}\t{total_words}\t{total_characters}\t{total_occurrences} total")
#         else:
#             output = ''
#             if args.lines:
#                 output += f"{total_lines} "
#             if args.words:
#                 output += f"{total_words} "
#             if args.characters:
#                 output += f"{total_characters} "
#             if args.occurrences:
#                 output += f"{total_occurrences} "
#             print(output.strip(), "total")

# if __name__ == '__main__':
#     main()




#Can be improved occurences but still
# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def count_occurrences(text, word):
#     return text.split().count(word)

# def process_file(file_path, occurrences_word=None):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             character_count = count_characters(text)
#             word_count = count_words(text)
#             line_count = count_lines(text)
#             occurrences_count = count_occurrences(text, occurrences_word) if occurrences_word else 0
#             return line_count, word_count, character_count, occurrences_count
#     except Exception as e:
#         return f"Error: {e}"

# def print_output(file_path, args, *counts):
#     if args.occurrences and len(counts) == 4:
#         print(f"Occurrences of {args.occurrences} in {file_path}: {counts[-1]}")
#     else:
#         output = ''
#         if args.lines:
#             output += f"{counts[0]}\t"
#         if args.words:
#             output += f"{counts[1]}\t"
#         if args.characters:
#             output += f"{counts[2]}\t"
#         if args.occurrences and len(counts) == 4:
#             output += f"{counts[3]}\t"
#         print(output.strip(), file_path)

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('files', nargs='*', type=str, help='Files to count')
#     parser.add_argument('-l', '--lines', action='store_true', help='Count only lines')
#     parser.add_argument('-w', '--words', action='store_true', help='Count only words')
#     parser.add_argument('-c', '--characters', action='store_true', help='Count only characters')
#     parser.add_argument('-occurrences', type=str, help='Count occurrences of a specific word')

#     args = parser.parse_args()

#     if not args.files:
#         print("Error: At least one file must be specified.")
#         sys.exit(1)

#     total_counts = [0, 0, 0, 0]

#     for file_path in args.files:
#         result = process_file(file_path, args.occurrences)

#         if isinstance(result, tuple):
#             print_output(file_path, args, *result)
#             total_counts = [sum(x) for x in zip(total_counts, result)]
#         else:
#             print(result)

#     if len(args.files) > 1:
#         print_output("total", args, *total_counts)

# if __name__ == '__main__':
#     main()






# Occurrences and other exten working fine but giving onlynumbers
# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def count_occurrences(text, word):
#     return text.split().count(word)

# def process_file(file_path, occurrences_word=None):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             character_count = count_characters(text)
#             word_count = count_words(text)
#             line_count = count_lines(text)
#             occurrences_count = count_occurrences(text, occurrences_word) if occurrences_word else 0
#             return line_count, word_count, character_count, occurrences_count
#     except Exception as e:
#         return f"Error: {e}"

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('files', nargs='*', type=str, help='Files to count')
#     parser.add_argument('-l', '--lines', action='store_true', help='Count only lines')
#     parser.add_argument('-w', '--words', action='store_true', help='Count only words')
#     parser.add_argument('-c', '--characters', action='store_true', help='Count only characters')
#     parser.add_argument('-occurrences', type=str, help='Count occurrences of a specific word')

#     args = parser.parse_args()

#     if not args.files:
#         print("Error: At least one file must be specified.")
#         sys.exit(1)

#     total_lines, total_words, total_characters, total_occurrences = 0, 0, 0, 0

#     for file_path in args.files:
#         result = process_file(file_path, args.occurrences)

#         if isinstance(result, tuple):
#             lines, words, characters, occurrences = result
#             total_lines += lines
#             total_words += words
#             total_characters += characters
#             total_occurrences += occurrences

#             if not args.lines and not args.words and not args.characters:
#                 print(f"{lines}\t{words}\t{characters}\t{occurrences} {file_path}")
#             else:
#                 output = ''
#                 if args.lines:
#                     output += f"{lines} "
#                 if args.words:
#                     output += f"{words} "
#                 if args.characters:
#                     output += f"{characters} "
#                 if args.occurrences:
#                     output += f"{occurrences} "
#                 print(output.strip(), file_path)
#         else:
#             print(result)

#     if len(args.files) > 1:
#         if not args.lines and not args.words and not args.characters:
#             print(f"{total_lines}\t{total_words}\t{total_characters}\t{total_occurrences} total")
#         else:
#             output = ''
#             if args.lines:
#                 output += f"{total_lines} "
#             if args.words:
#                 output += f"{total_words} "
#             if args.characters:
#                 output += f"{total_characters} "
#             if args.occurrences:
#                 output += f"{total_occurrences} "
#             print(output.strip(), "total")

# if __name__ == '__main__':
#     main()





# Extension with occurrences but not working correctly
# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def count_occurrences(text, word):
#     return text.split().count(word)

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('files', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
#                         help='Files to count (default: standard input)')
#     parser.add_argument('-occurrences', type=str, help='Count occurrences of a specific word')
#     parser.add_argument('-l', action='store_true', help='Count lines only')
#     parser.add_argument('-w', action='store_true', help='Count words only')
#     parser.add_argument('-c', action='store_true', help='Count characters only')

#     args = parser.parse_args()

#     total_lines = 0
#     total_words = 0
#     total_characters = 0

#     for file in args.files:
#         text = file.read()

#         if args.occurrences:
#             occurrences = count_occurrences(text, args.occurrences)
#             print(f'Occurrences of "{args.occurrences}" in {file.name}: {occurrences}')
#             continue

#         if args.l:
#             print(f"{count_lines(text)} {file.name}")
#         elif args.w:
#             print(f"{count_words(text)} {file.name}")
#         elif args.c:
#             print(f"{count_characters(text)} {file.name}")
#         else:
#             print(f"{count_lines(text)}\t{count_words(text)}\t{count_characters(text)} {file.name}")

#         total_lines += count_lines(text)
#         total_words += count_words(text)
#         total_characters += count_characters(text)

#     if len(args.files) > 1 and not args.occurrences:
#         if args.l:
#             print(f"{total_lines} total")
#         elif args.w:
#             print(f"{total_words} total")
#         elif args.c:
#             print(f"{total_characters} total")
#         else:
#             print(f"{total_lines}\t{total_words}\t{total_characters} total")

#     sys.exit(0)

# if __name__ == '__main__':
#     main()




#Extension without occurrences
# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def count_occurrences(text, word):
#     return text.split().count(word)

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('files', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
#                         help='Files to count (default: standard input)')
#     parser.add_argument('-occurrences', type=str, help='Count occurrences of a specific word')

#     args = parser.parse_args()

#     total_lines = 0
#     total_words = 0
#     total_characters = 0

#     for file in args.files:
#         text = file.read()

#         total_lines += count_lines(text)
#         total_words += count_words(text)
#         total_characters += count_characters(text)

#         if args.occurrences:
#             occurrences = count_occurrences(text, args.occurrences)
#             print(f'Occurrences of "{args.occurrences}" in {file.name}: {occurrences}')

#         print(f"{count_lines(text)}\t{count_words(text)}\t{count_characters(text)} {file.name}")

#     if len(args.files) > 1:
#         print(f"{total_lines}\t{total_words}\t{total_characters} total")

#     sys.exit(0)

# if __name__ == '__main__':
#     main()









# import argparse
# import sys

# def count_characters(text):
#     return len(text.encode('utf-8'))

# def count_words(text):
#     words = text.split()
#     return len(words)

# def count_lines(text):
#     return text.count('\n')

# def process_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             character_count = count_characters(text)
#             word_count = count_words(text)
#             line_count = count_lines(text)
#             return line_count, word_count, character_count
#     except Exception as e:
#         return f"Error: {e}"

# def main():
#     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
#     parser.add_argument('files', nargs='*', type=str, help='Files to count')
#     parser.add_argument('-l', '--lines', action='store_true', help='Count only lines')
#     parser.add_argument('-w', '--words', action='store_true', help='Count only words')
#     parser.add_argument('-c', '--characters', action='store_true', help='Count only characters')

#     args = parser.parse_args()

#     if not args.files:
#         print("Error: At least one file must be specified.")
#         sys.exit(1)

#     total_lines, total_words, total_characters = 0, 0, 0

#     for file_path in args.files:
#         result = process_file(file_path)

#         if isinstance(result, tuple):
#             lines, words, characters = result
#             total_lines += lines
#             total_words += words
#             total_characters += characters

#             if not args.lines and not args.words and not args.characters:
#                 print(f"{lines}\t{words}\t{characters} {file_path}")
#             else:
#                 output = ''
#                 if args.lines:
#                     output += f"{lines} "
#                 if args.words:
#                     output += f"{words} "
#                 if args.characters:
#                     output += f"{characters} "
#                 print(output.strip(), file_path)
#         else:
#             print(result)

#     if len(args.files) > 1:
#         if not args.lines and not args.words and not args.characters:
#             print(f"{total_lines}\t{total_words}\t{total_characters} total")
#         else:
#             output = ''
#             if args.lines:
#                 output += f"{total_lines} "
#             if args.words:
#                 output += f"{total_words} "
#             if args.characters:
#                 output += f"{total_characters} "
#             print(output.strip(), "total")

# if __name__ == '__main__':
#     main()















# # import argparse
# # import sys

# # def count_file_statistics(file):
# #     with open(file, 'r') as f:
# #         text = f.read()
# #         characters = len(text.encode('utf-8'))
# #         words = len(text.split())
# #         lines = text.count('\n')
# #         return lines, words, characters

# # def print_statistics(file, lines, words, characters):
# #     print(f"{lines}\t{words}\t{characters}\t{file}")

# # def main():
# #     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
# #     parser.add_argument('files', nargs='*', type=str, default=[],
# #                         help='Files to count (default: standard input)')

# #     args = parser.parse_args()

# #     total_lines, total_words, total_characters = 0, 0, 0

# #     for file in args.files:
# #         lines, words, characters = count_file_statistics(file)
# #         print_statistics(file, lines, words, characters)
# #         total_lines += lines
# #         total_words += words
# #         total_characters += characters

# #     if len(args.files) > 1:
# #         print(f"{total_lines}\t{total_words}\t{total_characters}\ttotal")

# # if __name__ == '__main__':
# #     main()













# # import argparse
# # import sys

# # def count_characters(text):
# #     return len(text.encode('utf-8'))

# # def count_words(text):
# #     words = text.split()
# #     return len(words)

# # def count_lines(text):
# #     return text.count('\n')

# # def main():
# #     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
# #     parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
# #                         help='File to count (default: standard input)')

# #     args = parser.parse_args()

# #     try:
# #         text = args.file.read()
# #     except Exception as e:
# #         print(f"Error: {e}")
# #         sys.exit(1)

# #     character_count = count_characters(text)
# #     word_count = count_words(text)
# #     line_count = count_lines(text)

# #     # Print the output in the format "line_count word_count character_count"
# #     print(f"{line_count}\t{word_count}\t{character_count}", end='')

# #     sys.exit(0)

# # if __name__ == '__main__':
# #     main()

# # import argparse
# # import sys

# # def count_characters(text):
# #     return len(text.encode('utf-8'))

# # def count_words(text):
# #     words = text.split()
# #     return len(words)

# # def count_lines(text):
# #     return text.count('\n')

# # def main():
# #     parser = argparse.ArgumentParser(description='Word count utility (wc) in Python')
# #     parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
# #                         help='File to count (default: standard input)')

# #     args = parser.parse_args()

# #     try:
# #         text = args.file.read()
# #     except Exception as e:
# #         print(f"Error: {e}")
# #         sys.exit(1)

# #     character_count = count_characters(text)
# #     word_count = count_words(text)
# #     line_count = count_lines(text)

# #     # Print the output in the format "line_count word_count character_count filename"
# #     print(f"{line_count}\t{word_count}\t{character_count}", end='')

# #     # Print the filename if reading from a file
# #     if args.file.name != '<stdin>':
# #         print(f" {args.file.name}", end='')

# #     sys.stdout.flush()  # Ensure the output is flushed to stdout

# #     print()  # Add a newline at the end

# #     sys.exit(0)

# # if __name__ == '__main__':
# #     main()