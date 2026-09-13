class Solution:
    '''
    - Init record
    - Iterate over each op in operations:
        if = "+": add new score that is sum of record[length-1] + record[length - 2]
        elif = "D": add new score that = record[length-1]*2
        elif = "C": record.pop()
        else: add to record
    - For i in range(len(record)), pop off the record and add to sum
    '''
    def calPoints(self, operations: List[str]) -> int:
        # Initiatie record stack
        record = []
        # Iterate over each op in operations:
        for op in operations:
            if op == "+":
                record.append(record[len(record)-1] + record[len(record) - 2])
            elif op == "D":
                record.append(record[len(record)-1] * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        # Pop off each element in the record and add to sum
        res = 0
        for i in range(len(record)):
            res += record.pop()
        return res




        