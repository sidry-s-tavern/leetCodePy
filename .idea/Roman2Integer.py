from re import match


class Solution:
    def romanToInt(self, s: str) -> int:
        Solution.romanToIntChar(Solution,'I')
        return -1

    def romanToIntChar(self, s: str) -> int:
        match s:
            case "I":
                print('I')
            case "V":
                print('V')
            case _:
                print('-1')
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
#
# public int romanToIntChar(char c) {
#   return switch (c) {
#       case 'I' -> 1;
#       case 'V' -> 5;
#       case 'X' -> 10;
#       case 'L' -> 50;
#       case 'C' -> 100;
#       case 'D' -> 500;
#       case 'M' -> 1000;
#       default -> -1;
#   };
# }
