class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        ans = 0
        while i < len(s) and s[i]==' ':
            i+=1
       
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            ans = (ans * 10) + int(s[i])
            i+=1
        result = ans * sign
        if result < -2**31 or result > 2**31-1:
            return -2**31 if result < -2**31 else 2**31-1
        return result
        # s = self.remove_whitespace(s)
        # word_arrs = s.split(" ")
        # for word in word_arrs:
        #     try:
        #         parsed_num = int(float(word))
        #         if parsed_num < -2**31 or parsed_num > 2**31-1:
        #             return -2**31 if parsed_num < -2**31 else 2**31-1
        #         else:
        #             return parsed_num
        #         # return parsed_num if -2**31 <= parsed_num <= 2**31 - 1 else 0
        #     except:
        #         return 0
    
x = Solution()

print(x.myAtoi(""))