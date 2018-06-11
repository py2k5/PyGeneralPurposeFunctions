def longest_substr_palinfrome(s):
    longestpalindrome = ""

    for i in range(1, len(s)):
        for j in range(0, i):
            array = s[j:i + 1]
            if array == array[::-1] and len(longestpalindrome) < len(array):
                longestpalindrome = array

    return longestpalindrome

print(longest_substr_palinfrome('mmadamssd'))
