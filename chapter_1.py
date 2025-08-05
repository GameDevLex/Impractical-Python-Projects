import sys, random

def funny_name_generator():
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

def pig_latin():
    while True:
        input_word = input("Word to convert to pig latin: ")
        pig_latin = ""
        for i in reversed(input_word):
            pig_latin = pig_latin + i
        pig_latin = pig_latin + "ay"
        print(pig_latin)

        input_word = input("Continue? (Write cancel to close)")
        if input_word.lower() == "cancel":
            break
        else:
            pass

def poor_man_bar_chart():
    # etaoin

    e_list = []
    t_list = []
    a_list = []
    o_list = []
    i_list = []
    n_list = []

    input_word = input("Phrase: ")

    for i in input_word:
        if i == "e":
            e_list.append(i)
        elif i == "t":
            t_list.append(i)
        elif i == "a":
            a_list.append(i)
        elif i == "o":
            o_list.append(i)
        elif i == "i":
            i_list.append(i)
        elif i == "n":
            n_list.append(i)
        else:
            pass

    print("e_list: " + str(e_list))
    print("t_list: " + str(t_list))
    print("a_list: " + str(a_list))
    print("o_list: " + str(o_list))
    print("i_list: " + str(i_list))
    print("n_list: " + str(n_list))

if __name__ == '__main__':
    funny_name_generator()
    pig_latin()
    poor_man_bar_chart()