"""
Vilhelmiina Rannikko, H290652
Ohjelmointi 1 / Programming 1 / COMP.CS.100
Projekti 3 / Project 3 - Kurssirekisteri / Course registry
Ohjelma on interaktiivinen kurssirekisteri, jossa voi syöttää/muokata/katsoa
rekisterin tietoja.
The program is an interactive course registry in which editing, user inputs
and viewing registry information is possible.
(Kommentit & muuttujat itse ohjelmassa ovat englanniksi.)
(All comments & variables in the program are in English.)
"""


def command_a(registry, command):
    """Adds the given course or department to the course registry.

    :param registry: dict
    :param command:, lst
    :return:
    """

    # Contents of 'command' are split in to parts and assigned to variables.
    # The method .pop is used to get rid of values that are already assigned.

    try:
        department = command[1]
        credit = int(command[-1])
        command.pop(0)
        command.pop(0)
        command.pop(-1)
        course = " ".join(command)

        if department not in registry:
            registry[department] = {}
            registry[department][course] = credit
            print(f"Added department {department} with course {course}")

        else:
            registry[department][course] = credit
            print(f"Added course {course} to department {department}")

    except ValueError:
        print("Invalid command!")


def command_p(registry):
    """Prints everything in the course registry under their respective
    departments.

    :param registry: dict
    :return:
    """

    print()
    for department in sorted(registry):
        print(f"*{department}*")
        for course in sorted(registry[department]):
            print(f"{course} : {registry[department][course]} cr")


def command_r(registry, command):
    """Prints all courses and their credits under the department given as
    input.

    :param registry: dict
    :param command: str
    :return:
    """
    department = command

    try:
        if department in registry:
            print()
            print(f"*{department}*")
            for course in sorted(registry[department]):
                print(f"{course} : {registry[department][course]} cr")
        else:
            print("Department not found!")

    except KeyError:
        print("Department not found!")


def command_d(registry, command):
    """Deletes the given course or department from the course registry.

    :param registry: dict
    :param command:, lst
    :return:
    """
    if len(command) == 2:
        try:
            department = command[1]
            del registry[department]
            print(f"Department {department} removed.")

        except KeyError:
            print(f"Department {department} not found!")

    else:
        try:
            department = command[1]
            # Removing assigned or useless values from 'command'.
            command.pop(0)
            command.pop(0)
            course = " ".join(command)
            del registry[department][course]
            print(f"Department {department} course {course} removed.")

        except KeyError:
            print(f"Course {course} from {department} not found!")


def command_c(registry, command):
    """Counts and prints how much credits are in a given department.

    :param registry: dict
    :param command:, lst
    :return:
    """
    department = str(command[1])

    credit = 0
    if department in registry:
        for subject in registry[department]:
            credit += int(registry[department][subject])
        print(f"Department {department} has to offer {credit} cr.")
    else:
        print("Department not found!")


def read_file(file):
    """Checks if every line in given file is three parts separated by a
    semicolon, and saves the file in to a dictionary within a dictionary.

    :param file: .txt file
    :return: registry: dict
    """

    registry = {}

    # The loop simultaneously checks that all rows are written correctly, and
    # assigns every course to a department, or creates a new department.

    for line in file:
        line = line.rstrip()
        row = line.split(";")
        if len(row) != 3:
            print("Error in file!")
            return None
        if row[0] not in registry:
            registry[row[0]] = {}
            registry[row[0]][row[1]] = int(row[2])
        else:
            registry[row[0]][row[1]] = int(row[2])

    return registry


def main():

    # The program opens a file and prints a notice if an error occurs.

    filename = input("Enter file name: ")
    try:
        file = open(filename, mode="r")
    except OSError:
        print(f"Error opening file!")
        return

    # The function read_file checks that all the lines in the file are valid
    # and good to use, and saves them to a dict within a dict. The file is
    # closed. If the variable is assigned None, the program ends.

    registry = read_file(file)
    if registry is None:
        return

    file.close()

    # Commencing a loop to carry out user requests via commands.
    # The corresponding actions are performed in their respective functions.

    while True:
        # The available user commands are printed.

        print("[A]dd / [C]redits / [D]elete / [P]rint all", end="")
        print(" / p[R]int department / [Q]uit")

        command = input("Enter command: ")
        command = command.split()

        if command[0] == "a":

            command_a(registry, command)

        elif command[0] == "c" and len(command) == 2:

            command_c(registry, command)

        elif command[0] == "d":

            command_d(registry, command)

        elif command[0] == "p":

            command_p(registry)

        elif command[0] == "r":

            command_r(registry, command[1])

        elif command[0] == "q":
            print("Ending program.")
            return

        else:
            print("Invalid command!")
            continue


if __name__ == "__main__":
    main()
