class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                try:
                    if haystack[i:i+len(needle)] == needle[:]:
                        return i
                except IndexError:
                    continue
