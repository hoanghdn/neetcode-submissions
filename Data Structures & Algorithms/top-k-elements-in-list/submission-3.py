class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort-- we first create a freq list where the index of the freq list is the "bucket" for numbers that appear i times. This works because we know the max number of times a number can appear is the length of the list. After, we'll go through the numbers and count how many times they appear, putting them into a dict. Then we take the dict and use dict.items to sort everything into the buckets. Finally, we go backwards in the frequency list to get k most frequent.

        count = {}
        frequency_list = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0) # count.get = either get the count[num if it exists, otherwise it's 0]

        # Here, count is the final dict. So we want to go through 
        for num, cnt in count.items():
            frequency_list[cnt].append(num) # what if we += here
        
        # now walk backwards
        res = []
        for i in range(len(frequency_list) - 1, 0, -1):
            for num in frequency_list[i]:
                res.append(num)
                if len(res) == k:
                    return res


