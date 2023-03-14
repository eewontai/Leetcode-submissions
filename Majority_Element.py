class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        for x in dict:
            if dict[x] > (len(nums))/2:
                return x
