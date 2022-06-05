#!/usr/bin/python3
def no_c(my_string):
    """This function removes all characters c and C from a 
        string.

        Args:
            my_string: the string to be checked and modified

        Return: the new string

    """
    #new_string = list(my_string)
    
    #for i in range(len(new_string) - 1):
        #if new_string[i] == 'c' or new_string[i] == 'C':
            #del(new_string[i])
    
    # This block concatenates the elements of new_string back to a string
    #return_string = ""
    #for character in new_string:
        #return_string += character
    
    #print(return_string)

    table = {ord('c'): None, ord('C'): None}
    new_string = my_string.translate(table)
    return (new_string)
