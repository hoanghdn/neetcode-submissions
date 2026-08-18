class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap will go complement:index
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i]
            else:
                complement = target - nums[i]
                hash_map[complement] = i
