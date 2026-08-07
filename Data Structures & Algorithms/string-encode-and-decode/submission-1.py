class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for s in strs:
            size = len(s)
            encoded_string += f'{size}#{s}'

        return encoded_string

# time: O(m); m = sum of lengths of all strings, n = number of strings
# space: O(m + n)

    def decode(self, s: str) -> List[str]:

        decoded_strs = []   #hold the split strings in an array
        i = j = 0   #set indices to grab strings. i will move ahead j looking for #, and j will be the start of the encoded string length number
        while i < len(s):   #keep looping while there's characters to search 
            while s[i] != '#':  #keep incrementing i until we find a #
                i += 1
            string_len = int(s[j:i])    #then store the number. This is the string length
            string = s[i + 1: i + string_len + 1]   #grab the string
            decoded_strs.append(string) #then append the string as a decoded word
            j = i = i + string_len + 1  #finally, move j and i forward to search for another #

        return decoded_strs #same as input to self.encode

# time: O(m)
# space: O(m + n)