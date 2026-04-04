class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0        
        i = 0
        while(i < len(s)):
            if(s[i].isalnum() == False):
                s = s[:i] + s[i+1:]
                i -= 1
            i += 1
        print(s)
        end = len(s) - 1
        while(start < end):
            if(s[start].lower() != s[end].lower()):
                print(s[start])
                print(s[end])
                return False
            start += 1
            end -=1
        
        return True

        # 8
        