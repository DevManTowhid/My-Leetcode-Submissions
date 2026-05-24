class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = [""] * numRows
        flag = 0
        increasing = True

        for char in s:
            result[flag] += char
            if flag == 0:
                increasing = True
            elif flag == numRows - 1:
                increasing = False

            if increasing:
                flag += 1
            else:
                flag -= 1

        return "".join(result)
                

            