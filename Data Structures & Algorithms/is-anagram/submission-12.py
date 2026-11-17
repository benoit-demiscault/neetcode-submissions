class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) :
            return False

        dicts = {}
        dictt = {}

        #O(n)
        for i in range(len(s)) :
            dicts[s[i]] = dicts.get(s[i], 0) + 1
            dictt[t[i]] = dictt.get(t[i], 0) + 1

    

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
        
        