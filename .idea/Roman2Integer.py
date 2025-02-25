class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        con = False
        for i in range(len(s)):
            if con:
                con = False
                continue
            curr = Solution.romanToIntChar(s[i])
            print("i", i, "curr", curr)
            next = 0
            if i != (len(s) - 1):
                next = Solution.romanToIntChar(s[i + 1])
                print("next", next)
                if curr < next:
                    res = res + next - curr
                    con = True
                else:
                    res += curr
            else:
                res += curr
            print("res", res)
        return res

    def romanToIntChar(s: str) -> int:
        if s == 'I': return 1
        if s == 'V': return 5
        if s == 'X': return 10
        if s == 'L': return 50
        if s == 'C': return 100
        if s == 'D': return 500
        if s == 'M': return 1000
        return -1


print(Solution.romanToInt(Solution, "MCMXCIV"))
