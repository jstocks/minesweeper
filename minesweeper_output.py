"""
TCSS504 Jeffrey Stockman NetID: stockmaj
Group Assignment #1 - individual solution

minesweeper output file

Reads a file input from python terminal that contains one or more minefields.
This code solves each minefield by producing a proximity score overlaid on each
minefield.  This code outputs the solution to 'minesweeper_output.txt'

"""


import re
import sys


def read_input_file(input_content, output_file=None):
    lines = input_content.readlines()
    """ capture all the 1-3 digit numbers from input file into a list"""
    numbers = []
    for line in lines:
        if line[0].isdigit():
            numbers.append([int(s) for s in re.findall(r'-?\d+', line)])

    """ remove redundant brackets """
    numbers = [val for sublist in numbers for val in sublist]

    """ build array from first two integers in list"""
    field_count = 0
    for i in range(len(numbers)):
        """ base case if we see O O"""
        if numbers[0] == 0 and numbers[1] == 0:
            return
        else:
            """ create array based on first two integers in numbers array"""
            field_count += 1
            ny = numbers[0]
            nx = numbers[1]
            arr = []
            for row in range(1, ny+1):
                arr.append(list(lines[row]))  # copying the lines from input file
            for ele in arr:
                del ele[-1]  # deletes the "/n"

            """ proximity score array"""
            score = [[0 for x in range(nx)] for y in range(ny)]

            for r in range(ny):
                for col in range(nx):
                    # contains mine
                    if arr[r][col] == "*":
                        score[r][col] = -1
                        continue
                    # northwest
                    if r-1 >= 0 and col-1 >= 0 and arr[r-1][col-1] == "*":
                        score[r][col] = score[r][col] + 1
                    # north
                    if r-1 >= 0 and arr[r-1][col] == "*":
                        score[r][col] = score[r][col] + 1
                    # northeast
                    if r-1 >= 0 and col+1 <= nx-1 and arr[r-1][col+1] == "*":
                        score[r][col] = score[r][col] + 1
                    # west
                    if col-1 >= 0 and arr[r][col-1] == "*":
                        score[r][col] = score[r][col] + 1
                    # east
                    if col+1 <= nx-1 and arr[r][col+1] == "*":
                        score[r][col] = score[r][col] + 1
                    # southwest
                    if r+1 <= ny-1 and col-1 >= 0 and arr[r + 1][col - 1] == "*":
                        score[r][col] = score[r][col] + 1
                    # south
                    if r+1 <= ny-1 and arr[r+1][col] == "*":
                        score[r][col] = score[r][col] + 1
                    # Check southeast
                    if r+1 <= ny-1 and col+1 <= nx-1 and arr[r+1][col+1] == "*":
                        score[r][col] = score[r][col] + 1

            """ format integer array into string array """
            score_str = []
            for s in range(ny):
                score_str.append([])
                for t in range(nx):
                    score_str[s].append(str(score[s][t]))
            """ replace '-1' with '*' """
            for s, row in enumerate(score_str):
                for t, cell in enumerate(row):
                    if cell == "-1":
                        score_str[s][t] = "*"

            if output_file is not None:  # for unit testing
                """ print results to file"""
                if field_count == 1:
                    f = open(output_file, "w")
                    f.write("Field #" + str(field_count) + ":\n")
                    for row in score_str:
                        f.write("".join(row) + "\n")
                    f.close()
                elif field_count > 1:
                    f = open(output_file, "a")
                    f.write("\n")
                    f.write("Field #" + str(field_count) + ":\n")
                    for row in score_str:
                        f.write("".join(row) + "\n")
                    f.close()

            else:  # used to generate output file
                if field_count == 1:
                    print("Field #" + str(field_count) + ":")
                    for row in score_str:
                        print("".join(row))
                if field_count > 1:
                    print("")
                    print("Field #" + str(field_count) + ":")
                    for row in score_str:
                        print("".join(row))

            """ pop off the first two integers in numbers array"""
            numbers.pop(1)
            numbers.pop(0)
            """ pop off the last ny number of lines in lines array """
            r = ny
            while r >= 0:
                lines.pop(r)
                r -= 1


if __name__ == '__main__':
    read_input_file(sys.stdin)

