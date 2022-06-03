#!/usr/bin/python3
def element_at(my_list, idx):
    """This is a function that retrieves an element at
        an index.

        Args:
            my_list: a list object containing the elements
            idx: the index of the element to be retrieved

        Return: None if idx is negative or out of range,
               otherwise return element

    """
    for element in my_list:
        if idx < 0 or idx >= len(my_list):
            return (None)
        else:
            return (my_list[idx])
