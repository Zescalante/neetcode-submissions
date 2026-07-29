class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)  #hashmap to store groups of anagrams
        # make a each word a set and compare to the other words?

        for s in strs:      #iterate through each string in the input. O(m)
            counts = [0]*26 #array to hold count of each letter in given word
            for char in s:  #iterate through chars in the word 
                counts[ord(char) - ord('a')] += 1   #update counter array
            key = tuple(counts)     #convert the counts to tuple to use as key 
            lookup[key].append(s)   # add the key and string to the hashmap

        return [sub for sub in lookup.values()] #return a list of sublists with grouped anagrams

# time: O(m*n); m =  num of strings, n = length of longest string
# space: O(m)