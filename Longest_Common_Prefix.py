class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ""
        n = len(strs)
        k = 0
            
            
        for i in range(len(strs[0])):
            for j in range(n):
                try:
                    if strs[j][i] == strs[0][i]:
                        k += 1
                except IndexError:
                    break;
                    
            if k==n:
                s += strs[0][i]
            else:
                break
            k=0
            
        return s
