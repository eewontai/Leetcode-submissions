# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        if n==1:
            return 1
     
        while(i<=j):
            if isBadVersion((i+j)//2):
                j = (i+j)//2
                if not isBadVersion(j-1):
                    return j
            else:
                i = (i+j)//2
                if isBadVersion(i+1):
                    return i+1
