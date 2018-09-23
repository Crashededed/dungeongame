def start():
    # add descriptions etc.
    print("""start of adventure!\n\n""")
    cave()


def prompt():
    x = int(input("Type a command: "))
    return x

def cave():
    # cave
    print("you wake up in a dark cave,\nyou lay on an ancient altar,"
          "\nthere's a dim light coming from a hole in the wall\n"
          "1.examine the altar.\n2.examine the hole")
    command = prompt()
    if command == 1:
        altar()
    elif command == 2:
        hole()

def hole():



start()