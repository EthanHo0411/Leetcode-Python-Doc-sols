class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store each number upon meeting
        #check if target - current number is present 
        #return the corresponding pair of index

        seen = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in seen:
                return [seen[result], i]
            seen[num] = i

