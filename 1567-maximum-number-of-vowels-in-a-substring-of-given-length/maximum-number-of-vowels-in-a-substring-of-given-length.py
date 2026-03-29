class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = 0
        left = 0
        vowel = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for right in range(len(s)):
            if s[right] in vowels:
                vowel += 1

            if (right - left + 1) == k:
                max_vowel = max(max_vowel, vowel)
                if s[left] in vowels:
                    vowel -= 1
                left += 1

        return max_vowel