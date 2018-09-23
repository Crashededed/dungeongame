def start():
    # add descriptions etc.
    print("""start of adventure!\n\n""")
    cave()


def prompt():
    x = int(input("Type a command: "))
    x = int(input("\nType a command: "))
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
def cave1():
    # cave
    print("you are in a dark cave, you see an ancient altar,"
          "\nthere's a dim light coming from a hole in the wall\n"
          "1.examine the altar.\n2.examine the hole")
    command = prompt()
    if command == 1:
        altar()
    elif command == 2:
        hole()


def hole():
    print("the hole is shining as if there's something in it\n"
          "1.put your hand in the hole\n"
          "2.back off the hole\n")
    command = prompt()
    if command == 1:
        print("you find a key inside the hole, it's shining brightly\n\n")
        key="true"
        cave1()
    elif command == 2:
        cave1()


start()