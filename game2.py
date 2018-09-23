def start():
    # add descriptions etc.
    global key
    key = 0
    print("\nstart of adventure!")
    cave()


def prompt():
    x = int(input("\nType a command: "))
    return x

def cave():
    # cave

    print("\nyou wake up in a dark cave,\nyou lay on an ancient altar,"
          "\nthere's a dim light coming from a hole in the wall"
          "\n1.examine the altar."
          "\n2.examine the hole")
    command = prompt()
    if command == 1:
        altar()
    elif command == 2:
        hole()
    else:
        cave()

def cave1():
    # cave
    print("\nyou are in a dark cave, you see an ancient altar,"
          "\nthere's a dim light coming from a hole in the wall\n"
          "1.examine the altar.\n2.examine the hole")
    command = prompt()
    if command == 1:
        altar()
    elif command == 2:
        hole()
    else:
        cave1()


def hole():
    print("\nthe hole is shining as if there's something in it\n"
          "1.put your hand in the hole\n"
          "2.back off the hole\n")
    command = prompt()
    if command == 1:
        print("\nyou find a key inside the hole, it's shining brightly")
        global key
        key = 1
        cave1()
    elif command == 2:
        cave1()
    else:
        hole()

def altar():
    print("\nyou examine the altar.\nit is covered with markings and stains.\n"
          "it has a large hole in the middle of it"
          "\n1.examine the hole."
          "\n2.back off the altar")
    command=prompt()
    if command == 1:
        if key == 1:
            print("\nyou try the key you found in the hole\n"
                  "the altar rises into the ceiling and reveals a staircase below it")
            staircase()
        else:
            print("\nyou don't have anything to put in the hole.\nyou examine the altar again")
            altar()

    elif command == 2:
        cave1()
    else:
        altar()
def staircase():
    print("\nbelow the altar appears a staircase")
start()