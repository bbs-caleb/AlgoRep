object Solution {
    def finalValueAfterOperations(operations: Array[String]): Int = {
        var x = 0
        for (op <- operations) {
            if (op.contains("+")) x += 1 
            else x -= 1
        }

        x
    }
}