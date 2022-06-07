#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """This funciton prints the elements of the matrix

        Args:
            matrix: a matrix of integers

        Return: nothing

    """
    for row in matrix:
        for i in row:
            if i != row[-1]:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()
