"""Find the uniqe elements in a list of elements"""
def uniqueList(inp_list):
    uniq_list = list(set(inp_list))
    return uniq_list

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
