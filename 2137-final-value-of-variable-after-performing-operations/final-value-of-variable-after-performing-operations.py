class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '+' in element else -1 for element in operations)