class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # sliding window keep track of number of ones than if more than 1 zero keep going till back at 1 zero
        if 0 not in nums:
            del nums[0]
        right = 0
        left = 0
        ones = 0
        maxval = 0
        k = 1
        while(right < len(nums) and left <= right):
            if(nums[right] == 1):
                ones += 1
                right += 1
            else:
                if(k > 0):
                    k -= 1
                    right += 1
                else:
                    while(k < 1 and left < len(nums)):
                        if(nums[left] == 0):
                            k = 1
                        else:
                            ones -= 1
                        left += 1
            maxval = max(maxval, ones)
        return maxval