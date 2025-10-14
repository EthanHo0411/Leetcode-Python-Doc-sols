class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create two dictionary to store the frequency of the characters 
        #compare the dictionary at the end 
        #use defaultdict for auto initialisation to 0 

        from collections import defaultdict 
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for char in s:
            dict1[char]+=1
        for char in t:
            dict2[char] +=1 
        if dict1 == dict2:
            return True
        return False
