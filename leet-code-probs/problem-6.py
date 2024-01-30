class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for row in range(numRows)]
        step = -1
        index = 0
        for char in s:
            rows[index].append(char)
            if index == numRows - 1:
                step = -1
            elif index == 0:
                step = 1
            index += step 
        
        for row in range(numRows):
            rows[row]=''.join(rows[row])
        return ''.join(rows)

s = Solution()

print(s.convert("helloworld",3))