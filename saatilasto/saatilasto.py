"""
Vilhelmiina Rannikko, H290652
Ohjelmointi 1 / Programming 1 / COMP.CS.100
Projekti 2 / Project 2 - Säätilasto / Weather statistics
Ohjelma tutkii käyttäjäsyöttöisiä säitä ja niiden mediaani- sekä keskiarvoja.
The program analyzes user input temperatures and their median and mean values.
(Kommentit & muuttujat itse ohjelmassa ovat englanniksi.)
(All comments & variables in the program are in English.)
"""


def count_average(given_list):
    """Counts the average of all values in a given list.

    :param given_list: list, list of float values
    :return: float, the average of the list's values.
    """
    return sum(given_list) / len(given_list)


def count_median(given_list):
    """Determines the median value of a given list.

    :param given_list: list, list of float values
    :return: float, the median of the list's values.
    """
    # The oddness or evenness of len(given_list) is determined to find the
    # median value. Setting the value of the division happening inside ''if''
    # to "int" rounds the index to a desirable value.

    ordered_list = sorted(given_list)

    if len(ordered_list) % 2 == 0:
        mid_index1 = int(len(ordered_list) / 2)
        mid_index2 = int(len(ordered_list) / 2) - 1
        median = (ordered_list[mid_index1] + ordered_list[mid_index2]) / 2
        return median
    else:
        mid_index = int(len(ordered_list) / 2)
        return ordered_list[mid_index]


def over_median(given_list, median):
    """Prints all temperatures over and at median and their difference to it.

    :param given_list: list, a list that is given
    :param median: float, the median value of said list
    :return: none, all the function does is print.
    """

    avg = count_average(given_list)
    print("Over or at median were:")
    # The loop compares every index's value to the median and prints.

    for index in range(len(given_list)):
        if given_list[index] >= median:
            print(f"Day{index + 1:3}. {given_list[index]:5.1f}C "
                  f"difference to mean: {given_list[index] - avg:5.1f}C")


def under_median(given_list, median):
    """Prints all temperatures under median and their difference to it.

    :param given_list: list, a list that is given
    :param median: float, the median value of said list
    :return: none, all the function does is print.
    """

    avg = count_average(given_list)
    print("Under median were:")
    # The loop compares every index's value to the median and prints.

    for index in range(len(given_list)):
        if given_list[index] < median:
            print(f"Day{index + 1:3}. {given_list[index]:5.1f}C "
                  f"difference to mean: {given_list[index] - avg:5.1f}C")


def main():

    # The loop indexes all user inputs to ''temperatures''.
    temperatures = []
    all_days = float(input("Enter amount of days: "))
    repeats = 1
    while repeats <= all_days:
        temp1 = float(input(f"Enter day {repeats}. temperature in Celcius: "))
        temperatures.append(temp1)
        repeats += 1

    # The list's mean and median are determined in their respective functions.

    print()
    print(f"Temperature mean: {count_average(temperatures):.1f}C")
    print(f"Temperature median: {count_median(temperatures):.1f}C")

    # The functions "over_median" and "under_median" find the values both
    # under and over the median, and print them accordingly.

    print()
    over_median(temperatures, count_median(temperatures))

    print()
    under_median(temperatures, count_median(temperatures))


if __name__ == "__main__":
    main()
