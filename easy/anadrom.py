class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Remove spaces and convert to lowercase
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()
        
        return sorted(s) == sorted(t)
