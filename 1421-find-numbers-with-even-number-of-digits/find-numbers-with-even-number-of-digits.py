class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            print(str(num))
            if((len(str(num)))%2 == 0):
                count += 1
        return count