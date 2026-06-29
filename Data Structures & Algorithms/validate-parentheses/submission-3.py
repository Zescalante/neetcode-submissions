class Solution:
    def isValid(self, s: str) -> bool:
        diction = {"(": ")", "[": "]", "{": "}"}
        arr = []
        for i, char in enumerate(s):
            if char in ["(","[","{"]:
                arr.append(char)
                print(arr)
            elif char in [")","]","}"]:
            #     return False if (not arr or diction[arr[-1]] != char) 
            #     arr.pop()
                if len(arr) == 0:
                    return False
                elif char == diction[arr[-1]]:
                    arr.pop()
                else: 
                    return False
            # elif diction[arr[-1]] == char:
            # elif diction[arr[-1]] == char:
                # print('True')
                # arr.pop()
            # else:
            #     return False
            
        return True if len(arr) == 0 else False
        # return False

        # print(arr)
