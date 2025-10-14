class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use a hashset for storing existing numbers to check for duplicates 
        seen = set()
        for num in nums: 
            if num in seen:
                return True
            seen.add(num)
        return False