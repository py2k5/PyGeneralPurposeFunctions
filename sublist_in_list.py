##find the Sum of all sub lists in a list
#for example: l = [ 1,2,3]
#has sublist [1],[2],[3],[1,2],[2,3],[1,2,3]
#sum of all the elements: 1+2+3+1+2+2+3+1+2+3 = 20
##sublist is a contiguous elements in the list


def sublists(s):
    length = len(s)
    for size in range(1, length + 1):
        for start in range(0, (length - size) + 1):
            yield s[start:start+size]

foo = [1,2,3]
sub_l = list(sublists(foo))
res = sum([ item for row in sub_l for item in row ])
print(res)
