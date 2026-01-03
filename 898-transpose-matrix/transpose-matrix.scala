object Solution {
    def transpose(matrix: Array[Array[Int]]): Array[Array[Int]] = {
        matrix(0).indices
        .map(j => matrix.map(_(j)))
        .toArray
    }
}