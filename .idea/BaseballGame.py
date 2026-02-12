class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        int x -> Record a new score of x.
        '+' -> Record a new score that is the sum of the previous two scores.
        'D' -> Record a new score that is the double of the previous score.
        'C' -> Invalidate the previous score, removing it from the record.
        """
        if len(operations) == 0:
            return
        if len(operations) == 1:
            return operations
        records = []
        for i in operations:
            if i == "C":
                records.pop(len(records) - 1)
            elif i == "D":
                records.append(records[-1] * 2)
            elif i == "+":
                if len(records) > 1:
                    records.append(records[-1] + records[-2])
            else:
                records.append(int(i))

            print(records)
        if len(records) == 0:
            return 0

        sum = 0;
        for i in records:
            sum += i
        return sum

    def printcalPoints(self, operations: list[str]):
        print(Solution.calPoints(Solution, operations))


Solution.printcalPoints(Solution, ["5", "-2", "4", "C", "D", "9", "+", "+"])
