# LEETCODE PROBLEM:
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.



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
