"""
COMP.CS.100 Programming 1
9.7 Yhteystiedot
"""


def read_file(filename):
    """Reads the file and gives info.

    :param: filename
    :return: -
    """

    dudes = {}

    file = open(filename, mode="r")

    for line in file:
        try:
            line = line.rstrip()
            row = line.split(";")
            dudes[row[0]] = {}
            dudes[row[0]]["name"] = row[1]
            dudes[row[0]]["phone"] = row[2]
            dudes[row[0]]["email"] = row[3]
            dudes[row[0]]["skype"] = row[4]

        except KeyError:
            pass

    return dudes
