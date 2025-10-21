class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode in a way len + some delimeter + string with arbitrary char 
        # this way it avoids the need to dedicate a char for separation 
        # all char can be used for the string
        encoding = ""
        for strings in strs:
            length = str(len(strings))
            encoding +=  length 
            encoding += "#"
            encoding += strings
        return encoding
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 
        temp = ""
        while i < len(s):
            if s[i] != "#":
                temp+= s[i]
                i+=1 
                continue
            length = int(temp)
            temp = ""
            i +=1
            result.append(s[i: i+length])
            i += length
        return result


