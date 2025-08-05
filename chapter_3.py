import sys

def find_anagrams():
    anagrams = []
    first_input = input("Input first word: ")
    first_input_list = sorted(list(first_input.lower()))

    try:
        lines = []
        with open('dictionary.txt') as file:
            while line := file.readline():
                lines.append(line.rstrip())

        for line in lines:
            dictionary_word_list = sorted(list(line.lower()))

            if first_input_list == dictionary_word_list:
                anagrams.append(line)

        print(anagrams)
    except FileNotFoundError:
        print("Error: The file 'your_file.txt' was not found.")


if __name__ == '__main__':
    find_anagrams()