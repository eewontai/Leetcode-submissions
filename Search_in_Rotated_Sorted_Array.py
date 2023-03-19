# LEETCODE PROBLEM:
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# Constraints:
# 1 ≤ nums.length ≤ 5000
# -104 ≤ nums[i] ≤ 104
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -104 ≤ target ≤ 104.




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ###l = len(nums)
        
        if target not in nums:
            return -1
        else:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i

                
