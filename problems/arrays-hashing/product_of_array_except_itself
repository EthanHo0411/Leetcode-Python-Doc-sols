class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #two pass method 1. left side 2. right side
        productl = [1]
        for i in range(1, len(nums)):
            productl.append(nums[i-1]*productl[-1])
        
        productr = [1]
        for i in range(len(nums)-2, -1 , -1):
            productr.insert(0, productr[0]*nums[i+1])
        
        return list(map(lambda x,y : x*y, productl , productr))