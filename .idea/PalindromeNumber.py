class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range(len(x+"")):
            print((x+"")[i])
        return True

Solution.isPalindrome(123)
        # String xString = Integer.toString(x);
        # for (int i = 0; i < xString.length(); i++) {
        # if(xString.charAt(i) != xString.charAt(xString.length()-i-1)) return false;
        # }
        # return true;