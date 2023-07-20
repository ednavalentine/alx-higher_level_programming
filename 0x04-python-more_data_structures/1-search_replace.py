#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for ink in my_list:
        if ink == search:
            newlist.append(replace)
        else:
            newlist.append(ink)
    return newlist
