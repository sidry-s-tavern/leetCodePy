from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            if strs[0] == "":
                return ""
            else:
                return strs[0]
        con = Solution.getContainsToList(strs)
        if len(con) != len(strs): return ""
        return getShortestFromList(contains);
        # return ""

    def getContainsToList(strs: List[str]) -> List[str]:
        contain: List[str]
        for i in range(len(strs) - 1):
            temp = Solution.containsStartEach(strs[i], strs[i + 1])
            if temp != "":
                contain.__add__(temp)
        return contain

    def containsStartEach(curr: str, next: str):
        sub = ""
        lowest = min(len(curr), len(next))
        for i in range(lowest):
            if curr[i] == next[i]:
                sub = sub + curr[i]
            else:
                break
        return sub

    def getShortestFromList(strs: List[str]) -> str:
        temp = len(strs[0])
        tempStr = strs[0]
        for i in range(len(strs)):
            if temp > len(strs[i]):
                temp = len(strs[i])
                tempStr = strs[i]
        return tempStr

Solution.longestCommonPrefix(Solution, ['flower', 'flow', 'flight'])
