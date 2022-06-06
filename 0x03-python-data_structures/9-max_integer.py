#!/usr/bin/python3
def max_integer(my_list=[]):
    """This function finds the biggest number in
        a list.

        Args:
            my_list: the list to be traversed

        Return: the biggest number
    """
    # if my_list:
    #     num = my_list[0]
    #     for element in my_list:
    #         if num < element:
    #             num = element
    #     return num
    # else:
    #     return None

    if my_list:
        return sorted(my_list)[-1]
    else:
        return None