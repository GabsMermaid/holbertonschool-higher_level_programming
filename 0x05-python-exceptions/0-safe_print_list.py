#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        while a < x:
            print(my_list[a], end="")
            a += 1
        print()
        return(a)
    except IndexError:
        print()
        return(a)
