import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        dele = string.punctuation + string.whitespace
        rem = s.maketrans("","",dele)

        s = s.lower().translate(rem)
        revs = s[::-1]

        if revs == s:
            return True   

        return False