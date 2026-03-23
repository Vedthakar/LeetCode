class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        return str1[:gcd(len(str1), len(str2))]

#I should have used this solution of eucliand math and tried to find the gcd!
#What I made a mistake on was trying to find the sub string and verify the substring 
#instead should have just used the math of the lengths.

#If next time its a pattern question try this trick! 
#if str1 + str2 != str2 + str1:
#            return ""
#This will get rid of the need for verifying if its a substring or not!
