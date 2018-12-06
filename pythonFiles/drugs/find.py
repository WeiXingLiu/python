from drugList import List

def beginFetchDetail(search_key):
    haveMore = True
    list = List(search_key)

    while haveMore:
        isShowAll = list.begin()
        if isShowAll == True:
            haveMore = False
