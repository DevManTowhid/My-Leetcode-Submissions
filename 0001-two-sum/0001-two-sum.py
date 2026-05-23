class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen_map:
                return [seen_map[complement], i]
            seen_map[nums[i]] = i