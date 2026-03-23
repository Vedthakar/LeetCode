class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #Ved Thakar
        print(len(word1))
        p = 0
        solution = ""
        while(p < len(word1) and p < len(word2)):
            solution += word1[p]
            solution += word2[p]
            p+=1
        
        solution += word1[p:]
        solution += word2[p:]
        return solution
