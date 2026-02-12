class Solution:
    """
    is not done: 11 / 24 Time Limit Exceeded
    """
    def firstBadVersion(self, n: int) -> int:
        if Solution.isBadVersion(n):
            print(f"{n}->{n-1}")
            return Solution.firstBadVersion(Solution, n - 1)
        return n+1

    def isBadVersion(version: int) -> bool:
        if version <= 4:
            return False
        return True


print(Solution.firstBadVersion(Solution, 6))
