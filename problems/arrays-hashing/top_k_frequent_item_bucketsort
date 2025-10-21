class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #perform bucket sort 
        #first record the frequency of the characters inside dictionary 
        from collections import defaultdict 
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        #create the buckets, one for each freq, including 0 index
        # the size maximum is determiend by the size of the list
        buckets = [ [] for i in range(len(nums)+1)]
        #then place the characters into their corresponding bukcet index by frequency 
        for char in freq.keys():
            buckets[freq[char]].append(char)

        #append the number to the result list from the end 
        result = []
        temp = k
        i = len(buckets)-1
        while i >= 0 and k >0 :
            if not buckets[i]:
                i -=1
            else: 
                result.append(buckets[i].pop())
                k-=1
        return result