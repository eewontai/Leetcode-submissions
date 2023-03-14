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
