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

        decoded_strs = []
        i = j = 0
        while i < len(s):
            print('looking for #')
            print(s[i])
            while s[i] != '#':
                print('char not # yet')
                i += 1
                print(i)
            print(s[j:i])
            string_len = int(s[j:i])
            string = s[i + 1: i + string_len + 1]
            print(string)
            decoded_strs.append(string)
            j = i = i + string_len + 1
            print(j,i)
        print(decoded_strs)

        return decoded_strs #same as input to self.encode

# time: O(m)
# space: O(m + n)