class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        n = len(s) # length of the thing we want to iterate
        if n < len(t):
            return ""

        count, win_ = {}, {}
        res = [None, None]
        len_ = n
        for i in t:
            count[i] = count.get(i, 0) + 1
        have, need = 0, len(count)
        l = 0

        for r in range(n):
            # print("+++++++++++")
            # print(f"current = {s[r]}")
            if s[r] in count:
                win_[s[r]] = win_.get(s[r], 0) + 1

                if win_[s[r]] == count[s[r]]:
                    have += 1

                    # if have == need:
                    #     len_ = min(len_, r - l + 1)
                    #     res = [l, r+1]
                        # print(f"Result = {res}")


                    while have == need:
                        if len_ >= (r - l + 1):
                            len_ =  r - l + 1
                            res = [l, r+ 1]
                            # print(f"Result = {res}")
                            # print(f"len ={len_}")
                        # print(f"popping elt = {s[l]}")
                        if s[l] in count:
                            win_[s[l]] = win_.get(s[l], 0) - 1
                            # print(win_)
                        
                            if win_[s[l]] < count[s[l]]:
                                # print(f"Have = {have}, Need = {need}")
                                have -= 1
                        # print(f"left, right = {l}, {r}")
                        # print()
                        
                        l += 1

            # print(f"Have = {have}, Need = {need}")
            # print(win_)
            # print(f"left, right = {l}, {r}")

        l, r = res[0], res[1]
        # print(s[l: r])

        if r is not None: return s[l: r]
        return ""







