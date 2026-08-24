class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0

        nums.sort()
        i = 1
        max_len = 1
        lenght = 1
        while(i < len(nums)):
            if(nums[i] == nums[i-1] + 1):
                lenght += 1
            if(nums[i] > nums[i-1] + 1):
                lenght = 1
            if(max_len <= lenght):
                max_len = lenght
            i += 1

        return max_len