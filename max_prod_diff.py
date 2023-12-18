'''
Maximum Product Difference Between Two Pairs

The product difference between two pairs (a, b) and (c, d) is
 defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is
 (5 * 6) - (2 * 7) = 16.

Given an integer array nums, choose four distinct indices w, x, y,
 and z such that the product difference between pairs (nums[w], 
 nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference. 

Example 1:
Input: nums = [5,6,2,7,4]
Output: 34
'''
def maxProductDifference(self, nums):
    '''
    Implementation 1 using builtin sort function
    Runtime: 165 ms
    Memory: 14.39 mb
    '''

    nums.sort()
    return nums[len(nums)-1] * nums[len(nums)-2] - nums[0] * nums[1]
