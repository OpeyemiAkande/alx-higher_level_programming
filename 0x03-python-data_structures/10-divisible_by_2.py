#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """This function checks for numbers that are
        divisible by 2.
        
        Args:
            my_list: the list of numbers to be traversed
        Return: a new list of true or false
    
    """
    new_list = []
    for elem in my_list:
        if elem % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return (new_list)
