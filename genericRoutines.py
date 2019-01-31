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
    	    print("{}:{}".format(x,inp_list.count(x)), end=",")
    	    s.add(x)

"""test the function
countOccurancesInList([1,2,3,4,3,2,3,5,6,2,3,5,2,4,6,32,5,1,43,32,2,3,4,21,1,2,4,45,32,1,3,0])
output:
1:4,2:6,3:6,4:4,5:3,6:2,32:3,43:1,21:1,45:1,0:1

"""

############### OR ###############
def countOccurancesInList(l):
    d = {}
    for item in l:
        if item in d:
            d[item] = d[item] + 1
        else:
            d[item] = 1

    print(d)

    ##OR
    
def countOccurancesInList(l):
    d = {}
    for item in l:
        try:
            d[item] = d[item] + 1
        except:
            d[item] = 1

    print(d)
    
    
    #OR
    
 def countOccurancesInList(l):
    d = {}
    for item in l:
        d[item] = d.get(item, 0) + 1
        
    print(d)

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
    
    ####OR####
    mi = {v:k for k,v in m.items()}
    print(mi)
    
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
invert_dict(m)
#####################################################################################################################  
"""Flateen a multidimensional list to one dimensional list 
   for example: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
def flatten_list(l):

    ##method 1 using comprehension
    res = [ item for row in l for item in row ]
    print(res)
    ##method 2 using loop
    res = []
    for row in l:
        for item in row:
            res.append(item)

    print(res)
#####################################################################################################################      
"""create a list of anagrams from a list of strings 
For example:  ['eat', 'ate', 'done', 'tea', 'soup', 'node']
           => [['done', 'node'], ['eat', 'ate', 'tea'], ['soup']]
"""        
def anagram(words):
    anagrams = {}
    for word in words:
        sword = ''.join(sorted(word))
        try:
            anagrams[sword].append(word)
        except KeyError:
            anagrams[sword] = [word]
    anagrams_list = [v for v in anagrams.values() ]
    print(anagrams_list)

words = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
anagram(words)
#####################################################################################################################     

###Given a string, repeatedly remove adjacent pairs of matching characters and then print the reduced result.
##aaabccddd → abccddd
##abccddd → abddd
##abddd → abd

def super_reduced_string(s):
    if not s:
        return 'Empty String'
    stack = ''
    for i, c in enumerate(s):
        if stack and stack[-1] == c:
            stack = stack[:-1]
        else:
            stack += c
    if stack:
        return stack
    return 'Empty String'
print(super_reduced_string('aaabccddd')    )

OR

def super_reduced_string(s):
    stack = []
    for i,c in enumerate(s):
        if not stack or c != stack[-1]:
            stack.append(c)
        else:
            stack.pop()
    if stack:
        return  ''.join(stack)
    else:
        return 'Empty String'
print(super_reduced_string('aaabccddd')    )


###########################################################################################################################
#we want to write a program that takes a list of filenames as arguments and to print only the line which has a particular substring, 
like grep command in unix.
def readfiles(filenames):
    for f in filenames:
        with open(f) as fr:
            for line in open(fr):
                yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print(line)

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)
