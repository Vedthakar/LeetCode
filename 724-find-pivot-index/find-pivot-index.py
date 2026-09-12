class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        val = -1
        maxval = -1
        for i in range(len(nums)):
            if(sum(nums[i+1:]) == sum(nums[:i])):
                return i
                val = i
        return maxval