class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range(len(str(x))):
            if str(x)[i]!=str(x)[-i-1]: return False
        return True

print(Solution.isPalindrome(Solution,1233221))
        # String xString = Integer.toString(x);
        # for (int i = 0; i < xString.length(); i++) {
        # if(xString.charAt(i) != xString.charAt(xString.length()-i-1)) return false;
        # }
        # return true;