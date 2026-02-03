# Good question
# Use Binary search and find middle
# find if it's first of the same element and second of the same element. check if it's odd position or even position. 
# 4 cases are there. if it's odd and second same element -> single element appears in the left

# EDGE CASES: when checking mid-1 and mid+1, if it's first or last element, it will give index out of bound error. so, handle that

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        start = 0
        end = len(nums)-1

        if len(nums) == 1:
            return nums[0]

        while start <= end:
            mid = (start+end)//2
            if mid == 0 and nums[mid+1] != nums[mid]:
                return nums[mid]
            if mid == len(nums)-1 and nums[mid-1] != nums[mid]:
                return nums[mid]
            if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            elif (nums[mid-1] == nums[mid] and mid%2 == 0) or (nums[mid+1] == nums[mid] and mid%2 != 0):
                end = mid - 1
            elif (nums[mid-1] == nums[mid] and mid%2 != 0) or (nums[mid+1] == nums[mid] and mid%2 == 0):
                start = mid + 1
                
        return -1

if __name__ == "__main__":
    s = Solution()
    # 1 1 2
    print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
    print(s.singleNonDuplicate([3,3,7,7,10,11,11]))
    print(s.singleNonDuplicate([1,1,2]))
                
                