#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """This function modifies a copy of my_list

        Args:
            my_list: the list of elements
            idx: index of the element to be modified
            element: the new element

        Return: Original list if idx is negative of out of range,
                otherwise return the new list
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
