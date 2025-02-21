class Solution:
    def romanToInt(self, s: str) -> int:
        Solution.romanToIntChar(Solution,'I')
        return -1

    def romanToIntChar(self, s: str) -> int:
        match s:
            case 'I': return 1
            case 'V': return 5
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            case _: return -1
        return -1
#   public int romanToInt(String s) {
#       int res = 0;
#       for (int i = 0; i < s.length(); i++) {
#           int curr = romanToIntChar(s.charAt(i));
#           int next = 0;
#           if (i != s.length()-1) {
#               next = romanToIntChar(s.charAt(i + 1));
#               if (curr < next) {
#                   res = res + next - curr;
#                   i++;
#               } else {
#                   res += curr;
#               }
#           } else {
#               res += curr;
#           }
#       }
#       return res;
#   }
