1class Solution {
2public:
3    int searchInsert(vector<int>& nums, int target) {
4        int n = (int)nums.size();
5        int l = 0, r = n;
6
7        while (l < r) {
8            int mid = l + (r - l) / 2;
9            if (nums[mid] < target) {
10                l = mid + 1;
11            } else {
12                r = mid;
13            }
14        }
15        return l;
16    }
17};