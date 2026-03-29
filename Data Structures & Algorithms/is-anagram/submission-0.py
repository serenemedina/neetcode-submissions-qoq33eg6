class Solution:
    def isAnagram(self, s: str, t: str) -> bool:            

        # make sure the lengths of the strings are the same, impossible to be anagram if they are not
        if len(s) != len(t):
            return False
        
        # counting characters in both of the strings, create 2 hashmaps
        countS, countT = {}, {}

        # iterate through the string s, bc they are the same length
        for i in range(len(s)):
            # count the occurence of each character in string s
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # count the occurence of each character in string t
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # c is the key
        for c in countS:
            if countS[c] != countT.get(c, 0): # use the get function so it doesnt throw an error if the key isnt in there
                return False

        # it is an anagram
        return True