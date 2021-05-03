"""
TCSS504 Jeffrey Stockman NetID: stockmaj
Group Assignment #1 - individual solution

minesweeper input file

creates single or multiple minesweeper boards based on row, column, and
mine probability;  writes all [R C] and minefield to a file
'minesweeper_input.txt' to be read and solved by 'minesweeper_output.py'

"""

import random
import os


def create_board(n, m, p):
    """ creates a minefield array of user-input size (#rows, #cols, probability) """

    """ base case if [0 0] sized board is created"""
    if n == m == 0:
        f = open("minesweeper_input.txt", "w")
        f.write("0 0")
        return

    # n = int(input("Enter the number of rows: "))
    # m = int(input("Enter the number of columns: "))
    # prob = int(input("Enter the probability(0 - 100%) of encountering a mine: "))

    """ creates initial array of size n, m """
    arr = [["." for x in range(m)] for y in range(n)]

    """ iterative mine placement """
    num_mines = int(m * n * p)
    mine_count = 0
    while mine_count < num_mines:
        x2 = random.randint(0, (n - 1))
        y2 = random.randint(0, (m - 1))
        if arr[x2][y2] == "*":
            pass
        else:
            arr[x2][y2] = "*"
            mine_count += 1

    """" write minefield(s) to file (file can't exist)"""
    if not os.path.exists("minesweeper_input.txt"):
        """ No fields exist, write new file """
        f = open("minesweeper_input.txt", "w")
        f.write(str(n) + " " + str(m) + "\n")
        for row in arr:
            f.write("".join(row) + "\n")
        """ end file with '0 0' """
        f.write("0 0")
        f.close()

        """ input file already exists, append to it"""
    else:
        """ delete the last 0,0 in file """
        with open("minesweeper_input.txt") as f1:
            lines = f1.readlines()
            lines = lines[:-1]

        with open("minesweeper_input.txt", "w") as f2:
            f2.writelines(lines)

            f2.write(str(n) + " " + str(m) + "\n")
            for row in arr:
                f2.write("".join(row) + "\n")
            """ end file with '0 0' """
            f2.write("0 0")
        f2.close()

    """print the contents of the input.txt file"""
    g = open("minesweeper_input.txt", 'r')
    file_contents = g.read()
    print(file_contents)

# edge cases
# create_board(1, 1, 1)
# create_board(3, 5, .25)
# create_board(100, 100, .2)
# create_board(100, 100, 1)
#
# # random board creation
create_board(3, 5, .25)
create_board(5, 10, .5)
create_board(10, 8, .3)
create_board(25, 15, .15)
create_board(35, 75, .1)
create_board(85, 40, .8)
create_board(92, 25, .15)
create_board(45, 37, .34)
create_board(1, 100, .73)
create_board(100, 1, .15)