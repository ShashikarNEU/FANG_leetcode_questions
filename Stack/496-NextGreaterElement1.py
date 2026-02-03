# Monotonic Stack Pattern
from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Find index arr of nums2
        hashTableIndex = defaultdict(int)

        for i in range(len(nums2)):
            hashTableIndex[nums2[i]] = i

        # Apply monotonic decreasing stack algo for nums2
        res = [-1]*len(nums2)
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()
                res[index] = nums2[i]
            stack.append(i)
        
        # Traverse the nums1 arr, find the index of element and refer res arr for that index
        ans = [0]*len(nums1)
        for i in range(len(nums1)):
            index = hashTableIndex[nums1[i]]
            ans[i] = res[index]
        
        return ans