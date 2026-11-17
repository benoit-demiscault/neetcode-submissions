class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) :
            return False

        dicts = {}
        dictt = {}

        #O(n)
        for letter in s :
            dicts[letter] = dicts.get(letter, 0) + 1

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
        
        