def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return max(alist[-1], find_largest(alist[:-1]))

print(find_largest([5,1,8,7,2]))
