l = [ 1,2,3,4,3,2,6]

print(min([i for i,val in enumerate(l) if val == 2]))
print(max([i for i,val in enumerate(l) if val == 2]))
