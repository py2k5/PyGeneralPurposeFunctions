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

    
