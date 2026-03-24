class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idea is start and go through the list if you find a 0 than get the tr to go until non zero found. and just flip.
        if len(nums) <= 1:
            return
        p = 0
        tr = 0
        i = 0
        while(tr < len(nums)):
            if(nums[tr] != 0):
                print(p)
                i = nums[p]
                nums[p] = nums[tr]
                nums[tr] = i
                p += 1
                tr += 1
            else:
                tr += 1        