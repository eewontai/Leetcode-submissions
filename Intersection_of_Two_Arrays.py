# LEETCODE PROBLEM:
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                if nums1[i] in a:
                    continue
                else:
                    a.append(nums1[i])
            else:
                continue
                
        return a

    
