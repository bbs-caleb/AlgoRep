object Solution {
    def recoverOrder(order: Array[Int], friends: Array[Int]): Array[Int] = {
        val friendsSet = friends.toSet
        order.filter(friendsSet.contains)
    }
}