class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        l = len(y)
        for i in range(l):
            if y[i] != y[l-i-1]:
                return False
        return True
