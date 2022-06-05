#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """This is a function that replaces the element of an
        element in place.

        Args:
            my_list: the list to be modified
            idx: index of the element to be replaced
            element: the new element at the index idx

        Return: original list if idx is negative or out of range,
                otherwise returns the modified list

    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    my_list[idx] = element
    return (my_list)
