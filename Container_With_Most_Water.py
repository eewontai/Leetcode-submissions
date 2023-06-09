# LEETCODE PROBLEM: 
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = max( (j-i)*min(height[i], height[j]), area)
        return area
        '''
        head = 0
        tail = len(height) - 1
        water = 0
        x = 0 #temp var for storing water
        while(head<tail):
            if height[head] > height[tail]:
                x = (tail-head)*height[tail]
                tail -= 1
            else:
                x = (tail-head)*height[head]
                head += 1
            if x > water:
                water = x
                
        return water

    
