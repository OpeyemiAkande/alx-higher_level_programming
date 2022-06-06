#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """This function deletes an element at a given index (idx).

        Args:
            my_list: the list to be traversed
            idx: the index at which
        Return: nothing
    """
    new_idx = idx + 1
    new_list = my_list[:idx] + my_list[new_idx:]
    return new_list
