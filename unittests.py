from minesweeper_output import *
import unittest


class MinesweeperTests(unittest.TestCase):
    """
     Tests that the minesweeper_output.py generates the correct output
     by comparing the output file generated with the expected output file
     for a given input file.
     Tests are named in the format: row_col_mines(number or probability)
    """
    def test_1_1_1(self):
        # get the expected file content (manually create)
        with open('1_1_1_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('1_1_1_input.txt', 'r') as input_file:
            read_input_file(input_file, "1_1_1_prog_output.txt")

        # get the actual file content from the previous execution
        with open("1_1_1_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")

    def test_1_1_20(self):
        # get the expected file content (manually create)
        with open('1_1_20%_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('1_1_20%_input.txt', 'r') as input_file:
            read_input_file(input_file, "1_1_20%_prog_output.txt")

        # get the actual file content from the previous execution
        with open("1_1_20%_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")

    def test_1_1_100(self):
        # get the expected file content (manually create)
        with open('1_1_100%_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('1_1_100%_input.txt', 'r') as input_file:
            read_input_file(input_file, "1_1_100%_prog_output.txt")

        # get the actual file content from the previous execution
        with open("1_1_100%_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")

    def test_100_100_1(self):
        # get the expected file content (manually create)
        with open('100_100_1_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('100_100_1_input.txt', 'r') as input_file:
            read_input_file(input_file, "100_100_1_prog_output.txt")

        # get the actual file content from the previous execution
        with open("100_100_1_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")

    def test_100_100_20(self):
        # get the expected file content (manually create)
        with open('100_100_20%_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('100_100_20%_input.txt', 'r') as input_file:
            read_input_file(input_file, "100_100_20%_prog_output.txt")

        # get the actual file content from the previous execution
        with open("100_100_20%_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")
    #
    def test_100_100_100(self):
        # get the expected file content (manually create)
        with open('100_100_100%_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('100_100_100%_input.txt', 'r') as input_file:
            read_input_file(input_file, "100_100_100%_prog_output.txt")

        # get the actual file content from the previous execution
        with open("100_100_100%_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")

    def test_3_2_25(self):
        # get the expected file content (manually create)
        with open('3_5_25%_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('3_5_25%_input.txt', 'r') as input_file:
            read_input_file(input_file, "3_5_25%_prog_output.txt")

        # get the actual file content from the previous execution
        with open("3_5_25%_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")

    def test_two_field(self):
        # get the expected file content (manually create)
        with open('two_field_random_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('two_field_random_input.txt', 'r') as input_file:
            read_input_file(input_file, "two_field_random_prog_output.txt")

        # get the actual file content from the previous execution
        with open("two_field_random_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")

    def test_ten_field(self):
        # get the expected file content (manually create)
        with open('ten_field_random_expected_output.txt', 'r') as expected_file:
            expected_content = expected_file.read()

        # read the input file and pass in the function
        with open('ten_field_random_input.txt', 'r') as input_file:
            read_input_file(input_file, "ten_field_random_prog_output.txt")

        # get the actual file content from the previous execution
        with open("ten_field_random_prog_output.txt", 'r') as actual_file:
            actual_file_content = actual_file.read()

        self.assertEqual(actual_file_content, expected_content, "the contents are not the same")


if __name__ == '__main__':
    unittest.main()
