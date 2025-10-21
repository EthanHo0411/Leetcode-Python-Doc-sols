class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #identify the start of a consecutive list 
        #if the number doesn't have a number smaller than it, its a start
        #check the length of these possible start 

        sett = set(nums)
        maxlen = 0 
        for num in nums:
            length = 0
            if num -1 not in sett:
                length = 1
                temp = num
                while temp+1 in sett:
                    length += 1
                    temp += 1
                maxlen = max(maxlen, length)
        return maxlen

