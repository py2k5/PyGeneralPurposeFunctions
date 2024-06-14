##function to find the common longest palindrome between 2 strings
##approach is to find the longest palindrome in the shorter string and check if it exists in the longest string
## O(n2)


def longest_common_palindrome(s1, s2):
    palindrome_list = []
    max_palindrome=""
    source = ""
    target = ""
    if len(s1) > len(s2):
        source = s2
        target = s1
    else:
        source = s1
        target = s2
    for i in range(1, len(source)):
        for j in range(0, i):
            array = source[j: i + 1]
            if array == array[::-1]:
                palindrome_list.append(array)
    for palindrome in palindrome_list:
        if palindrome in target:
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome
    return max_palindrome

print(longest_common_palindrome('xysdjspottTOPSPOTdjhfbsdfajshbd','xysdjasdjhbatopTOPSPOTdjh'))

####OR simple

def longest_palindrome(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    longest = ''
    for i in range(len(s1)):
        for j in range(i+1, len(s1)+1):
            if s1[i:j] in s2 and len(s1[i:j]) > len(longest):
                longest = s1[i:j]
    return longest

print(longest_palindrome('rabc', 'abacdfgdcaba')) #ab
