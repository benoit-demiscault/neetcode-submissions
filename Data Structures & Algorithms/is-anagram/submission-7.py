class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}

        #O(n)
        for letter in s :
            if letter in dicts :
                dicts[letter] +=1
            else : 
                dicts[letter] = 1

        #O(m)        
        for letter in t :
            if letter in dictt :
                dictt[letter] +=1
            else : 
                dictt[letter] = 1

        return dictt == dicts
        """
        #O(max(n, m))
        if len(dicts) != len(dictt) : 
            return False

        for key, value in dicts.items():
            if key not in dictt : 
                return False
            if dictt[key] != value : 
                return False

        return True"""
        
        