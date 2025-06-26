class Solution(object):
    def twoSum(self, nums, target):
        nums_map = {}
        for p in range(len(nums)):
            if nums[p] in nums_map:
                return [nums_map[nums[p]], p]
            else:
                nums_map[target - nums[p]] = p
        return None