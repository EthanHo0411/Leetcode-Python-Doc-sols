class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #have two pointer starting at the end travelling towards center
        #since its in non-decreasing order, change the pointer index increase or descrease the total 

        i = 0 
        j = len(numbers) -1

        while i < j:
            total = numbers[i] + numbers[j]
            if total < target:
                i+=1
            elif total > target: 
                j-=1
            else:
                return [i+1, j+1]