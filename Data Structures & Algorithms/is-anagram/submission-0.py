class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # nlogn + mlogm
        ss = sorted(s) # nlogn
        ts = sorted(t) # mlogm

        return ss == ts
    

        

        
        
        
        