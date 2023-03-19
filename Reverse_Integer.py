# LEETCODE PROBLEM:
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        s1 = ""
        n = len(s)
        if x>=0:
            for i in range(-1, -n-1, -1):
                s1 += s[i]
            if int(s1)<-2**31 or int(s1)>2**31-1:
                return 0
            else:
                return int(s1)
        else:
            s1 += "-"
            for i in range(-1, -n, -1):
                s1 += s[i]
            if int(s1)<-2**31 or int(s1)>2**31-1:
                return 0
            else:
                return int(s1)
