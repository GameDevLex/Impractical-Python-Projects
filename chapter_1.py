import sys, random

if __name__ == '__main__':
    first_names = ("John", "Joey", "David", "Paul", "Nathan", "Ben")
    last_names = ("Rajan", "Tsu", "Kopf", "Paul", "Beer", "O'Connel")

    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        print("\n")
        print(first_name + " " + last_name, file=sys.stderr)
        print("\n")

        try_again = input("\n" + "Generate another random name? (Type exit to close app)" + "\n")
        if try_again == "exit":
            break
