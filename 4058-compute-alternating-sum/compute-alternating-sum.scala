object Solution {
    def alternatingSum(nums: Array[Int]): Int = {
        nums.zipWithIndex.map {case (num, i) => if (i % 2 == 0) num else -num}.sum
    }
}