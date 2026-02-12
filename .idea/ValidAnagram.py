class Solution:
    def printSolution(s:str, t:str):
        print(Solution.isAnagram(Solution, s, t))

    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False


Solution.printSolution("anagram","nagaram")