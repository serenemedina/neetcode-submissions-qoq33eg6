class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

# make sure the lengths of the strings are the same, impossible to be anagram if they are not
        if len(s) != len(t):
            return False
        
        # counting characters in both of the strings, create 2 hashmaps
        s_map, t_map = {}, {}

				# iterate through the string s, because they are the same length
        for i in range(len(s)):
        # count the occurence of each character in string s, and t
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
				
				# count is the key
        for count in s_map:
        # use the get function so it doesnt throw an error if the key isnt in there
            if s_map[count] != t_map.get(count, 0): 
                return False
                
        return True