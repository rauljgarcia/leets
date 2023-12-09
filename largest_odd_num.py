''''
1903. Largest Odd Number in String

You are given a string 'num', representing a large integer. 

Return the largest-valued odd integer (as a string) that is a
non-empty substring of num, or an empty string "" if no odd integer
exists.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52".
             "5" is the only odd number.

***Of my 3 implementations #2 was fastest
'''
def lrg_odd1(num):
    '''
    Implementation 1
        Time complexity: O(n)
        Space complexity: O(n)
    Results: 
        Runtime: beats 6.75% of users
        Memory: beats 39.14% of users
    '''
    result = ""
    for i in range(len(num)):
        if int(num[i])%2 == 1:
            result = num[:i+1]
    return result

def lrg_odd2(num):
    '''
    Implementation 2
        Time complexity: O(n)
        Space complexity: O(1)
    Results: 
        Runtime: beats 47.27% of users
        Memory: beats 18.68% of users
    '''
    if int(num[-1]) % 2 == 1:
        return num
    for i in range(-1, -len(num)-1, -1):
        if int(num[i]) % 2 == 1:
            return(num[:i+1])
    return ""

def lrg_odd3(num):
    '''
    Implementation 3
        Time complexity: O(n) - for both cases
        Space complexity: O(1) - for Case 1
        Space complexity: O(n) - for Case 2
    Results: 
        Runtime: beats 7.24% of users
        Memory: beats 67.7% of users
    '''
    # Case 1: last digit is odd
    if int(num[-1]) % 2 == 1:
            return num

    # Case 2: last digit is even
    result = ""
    for i in range(len(num)):
        if int(num[i])%2 == 1:
            result = num[:i+1]
    return result


#### LC's implementation ####
'''
Time complexity: O(n)
Space complexity: O(1)
'''
def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
            
        return ""