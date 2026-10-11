class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l = 0
        r = len(s1) - 1
        n = len(s2) - 1
        if r > n:
            return False
        
        while r <= n:
            # if sorted(s2[l : r + 1]) == s1:
            #     return True
            list_s2 = sorted(s2[l : r + 1])
            str_s2 = "".join(list_s2)
            if list_s2 == s1:
                return True
            # print("++++++++++")
            # print(list_s2)
            # print(l, r)

            l += 1
            r += 1
            

        return False