#####################################################################################################################
"""Find the uniqe elements in a list of elements"""
def uniqueList(inp_list):
    uniq_list = list(set(inp_list))
    return uniq_list

#####################################################################################################################
"""Generate a fibonacci series using a generator"""
def fibonacci_by_generator(num):
    a,b = 0,1
    for i in xrange(0,num):
        yield "{}:{}".format(i+1,a)
        a,b = b, a+b
        
"""
###calling the fibonacci function
   for item in fibonacci_by_generator(10):
       print(item)
"""
#####################################################################################################################

"""print the number and its count in a list in order of their appearances
example : [ 1,2,3,3,2,3,4,2,1] => 1:2,2:3,3:3,4:1 
"""
def countOccurancesInList(inp_list):
    s=set()
    for x in inp_list:
        if x in s:
            pass
        else:
    	    print(x,inp_list.count(x))
    	    s.add(x)

"""test the function
countOccurancesInList([1,2,3,4,3,2,3,5,6,2,3,5,2,4,6,32,5,1,43,32,2,3,4,21,1,2,4,45,32,1,3,0])
"""
#####################################################################################################################
"""Transpose a multidimensional list 
   for example -> [ [1,2,3],[4,5,6],[7,8,9] ]
   should be transposed to [ [1,4,7],[2,5,8],[3,6,9] ]
"""
def transpose(l):
    #method1
    res1 = [ [row[i] for row in l] for i in range(len(l)) ]
    
    #method2
    res2 = [ list(i) for i in zip(*l) ]
#####################################################################################################################    

"""Inverting a dictionary""""""
def invert_dict(m):
    print(m.items())
    ######[('a', 1), ('c', 3), ('b', 2), ('d', 4)]
    print(zip(m.values(), m.keys()))
    ####[(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
    mi = dict(zip(m.values(), m.keys()))
    print(mi)
    ###{1:'a',2:'b',3:'c',4:'d'}
    
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
invert_dict(m)
#####################################################################################################################  
