class Solution:
    def isPalindrome(self, s: str) -> bool:
        spec = ".,:;!?_*-+`()'[]\"\{/\#% &@}"
        for char in spec:
            if char in s:
                s = s.replace(char,"")
        s = s.lower()
        print(s)
        return s[::-1] == s


print(Solution.isPalindrome(Solution, s="A man, a plan, a canal: Panama"))
