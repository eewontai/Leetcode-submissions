# LEETCODE PROBLEM:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = list()
        for i in nums1:
            l.append(i)
        for j in nums2:
            l.append(j)
        l.sort()
        le = len(l)
        m = 0
        if le % 2 == 0:
            m = (l[le//2 - 1] + l[le//2]) / 2
        else:
            m = float(l[(le+1)//2 - 1])
        
        
        return m

    
