class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s.lower() if char.isalnum()])
        revs = s[::-1]
        
        if s == revs:
            return True

        return False