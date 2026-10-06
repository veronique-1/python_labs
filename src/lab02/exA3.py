def flatten(mat: list[list | tuple])-> list:
    res = []
    for i in mat:
        if type(i) == list or type(i) == tuple:
            res.extend(i)
        else:
            raise TypeError
    return res

print( flatten([[1, 2], [3, 4]]))
print( flatten([[1, 2], (3, 4, 5)]))
print( flatten([[1], [], [2, 3]]))
print( flatten([[1, 2], "ab"]))