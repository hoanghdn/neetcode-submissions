class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        starts = []
        max_count = 1

        # go through every number-- if it has no left neighbor, it's the start of a sequence.
        for num in num_set:
            if num-1 not in num_set:
                starts.append(num)
        
        for start in starts:
            curr_count = 1
            n = start
            while n+1 in num_set:
                curr_count += 1
                n += 1
                if curr_count >= max_count:
                    max_count = curr_count

        return max_count
