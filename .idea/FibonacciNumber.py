class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0;
        elif n < 3:
            return 1
        return Solution.fib(Solution, n - 1) + Solution.fib(Solution, n - 2)
