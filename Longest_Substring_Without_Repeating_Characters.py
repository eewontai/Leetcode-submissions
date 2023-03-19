class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = {}
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            a[i]=1
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    a[i] += 1
                else:
                    break
        return max(a.values())
    
    
    '''    
    if-break
    inside []s
    '''

    
