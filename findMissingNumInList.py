##This program finds a number missing in the list of 0 to N
##Example [1,4,2,0]
##output: 3
def sumMethod(inputList):
        # find (n*n+1)/2
        fullSum = (len(inputList) * (len(inputList) + 1)) / 2 
        # subtract sum of full range from supplied range
        return fullSum - sum(inputList)
print(sumMethod([1,2,3])) 



OR

def lookUpmethod(inputList):
        s = set(inputList)
        i = 1
        while i in s:
                i += 1
        return i

