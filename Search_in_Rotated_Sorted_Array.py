class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ###l = len(nums)
        
        if target not in nums:
            return -1
        else:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
