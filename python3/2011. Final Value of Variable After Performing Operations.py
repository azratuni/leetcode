class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X= 0
        for operation in operations:
            if operation == '--X':
                X = X-1
            if operation == 'X--':
                X = X-1
            if operation == 'X++':
                X = X+1
            if operation == '++X':
                X = X+1
        return X