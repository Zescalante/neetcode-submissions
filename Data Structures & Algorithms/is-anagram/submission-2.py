class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):   #first check if the strings are even equal
            return False       #if not, then they can't be anagrams

        diction = {}           #empty dictionary to store char, count of one of the strings

        for i, char in enumerate(s):    #go through one of the strings
            if char in diction:         #if the char is already in the hashmap
                diction[char] += 1      #then increment its counter
            else:                       #otherwise append it and start counter
                diction[char] = 1

        for char in t:                  #now loop through chars for the other string
            if char in diction and diction[char] > 0:         #if the character is in the dictionary
                diction[char] -= 1      #reduce the counter by one
            else:  #or if char not in diction or counter has gone negative
                return False            #then not an anagram
        return True                     #else, it's a valid anagram
        
