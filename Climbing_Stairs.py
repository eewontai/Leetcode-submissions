# LEETCODE PROBLEM: 
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0 for i in range(n+1)]
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        
        a[0] = 0
        a[1] = 1
        a[2] = 2
        
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2]
        
        
        return a[n]

    
