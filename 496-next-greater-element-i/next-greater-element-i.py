class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for x in nums2:
            while stack and stack[-1] < x:
                v = stack.pop()
                next_greater[v] = x
            stack.append(x)
        
        for v in stack:
            next_greater[v] = -1
        
        return [next_greater[v] for v in nums1]