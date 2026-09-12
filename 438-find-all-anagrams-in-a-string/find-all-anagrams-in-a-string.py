class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # fixed sliding window
        left = 0
        right = len(p)
        arra = []
        hasS = dict(Counter(s[left:right]))
        hasP = dict(Counter(p))
        while(right <= len(s)):
            if(hasS == hasP):
                arra.append(left)
            hasS[s[left]] -= 1
            if hasS[s[left]] == 0:
                del hasS[s[left]]
            left += 1

            if right < len(s):
                hasS[s[right]] = hasS.get(s[right], 0) + 1
            right += 1
        return arra