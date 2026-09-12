class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        maxval = 0
        val = 0
        for i in range(len(gain)):
            print("val =", val)
            print("current = ",current)
            val += gain[i]
            maxval = max(maxval, val)
        return maxval