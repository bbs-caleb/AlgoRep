object Solution {
    def finalValueAfterOperations(operations: Array[String]): Int = {
        operations.foldLeft(0) {(x, op) => if (op.contains("+")) x + 1 else x - 1}
    }
}