import sys


def scrape_palidrome():
    try:
        lines = []
        palindrome = []
        with open('dictionary.txt') as file:
            while line := file.readline():
                lines.append(line.rstrip())

        for line in lines:
            if line == line[::-1]:
                palindrome.append(line)
            else:
                pass
        print(palindrome)
    except FileNotFoundError:
        print("Error: The file 'your_file.txt' was not found.")


def scrape_palingram():
    try:
        lines = []
        palingram = []
        with open('dictionary.txt') as file:
            while line := file.readline():
                lines.append(line.rstrip())

        for line in lines:
            if (" " in line) and (line.replace(" ", "") == (line.replace(" ", ""))[::-1]):
                palingram.append(line)

        print(palingram)
    except FileNotFoundError:
        print("Error: The file 'your_file.txt' was not found.")



if __name__ == '__main__':
    scrape_palidrome()
    scrape_palingram()