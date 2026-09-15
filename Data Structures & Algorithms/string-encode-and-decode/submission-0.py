class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            n = len(i)
            string = string + str(n) + "$" + i 
            # string = string.join([str(n),i])
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0 
        digit = ""
        while i < len(s):

            if s[i].isdigit():
                digit = digit + s[i]
                i = i + 1 
            elif s[i] == "$":
                temp = ""
                i = i + 1
                for _ in range(int(digit)):
                    temp = temp + s[i]
                    i = i + 1
                l.append(temp)
                digit = ""
        return l
