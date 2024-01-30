# class Solution:
    
#     def isMatch(self, s: str, p: str) -> bool:
#         str_len = len(s)
#         s_idx =0
#         p_idx =0
#         valid = True
        
#         if len(s) > len(p):
#             return False

#         while s_idx < str_len:
#             char1 = s[s_idx]
#             char2 = p[p_idx]

#             obj = self.check(p,p_idx,char1,char2)
#             valid = obj["valid"]
#             p_idx = obj["p_idx"]
#             # print(s_idx,p_idx)
#             s_idx += 1
#         # Check if the remaining characters in pattern are all '*'
#         while p_idx < len(p) and p[p_idx] == '*':
#             p_idx += 1
            
        
#         return p_idx == len(p) and valid
    
#     def check(self,p:str,p_idx:int,char1:str,char2:str):
#         valid = True
        
#         if char1 != char2:
#             if char2 != "*" and char2 != ".":
#                 valid = False
#             elif char2 == "*":
#                 obj = self.check(p,p_idx , char1, p[p_idx - 1])
#                 valid = obj["valid"]
#                 p_idx = obj["p_idx"]
#             elif char2 == ".":
#                 p_idx += 1
#         else:
#             p_idx += 1

#         return dict(valid = valid,p_idx= p_idx)
    


# s = Solution()

# print(s.isMatch("aab","c*a*b"))


# class Solution:

#     def isMatch(self, s: str, p: str) -> bool:
#         s_len = len(s)
#         p_len = len(p)
#         s_idx = 0
#         p_idx = 0
#         valid = True

#         if len(s) > len(p):
#             return False

#         while s_idx < s_len and p_idx < p_len:
#             # if p_idx < len(p) and (s[s_idx] == p[p_idx] or p[p_idx] == '.'):
#             #     s_idx += 1
#             #     p_idx += 1
#             # elif p_idx < len(p) and p[p_idx] == '*':
#             #     if p_idx > 0 and (s[s_idx] == p[p_idx - 1] or p[p_idx - 1] == '.'):
#             #         s_idx += 1
#             #     else:
#             #         p_idx += 1
#             # elif p_idx + 1 < len(p) and p[p_idx + 1] == '*':
#             #     p_idx += 2
#             # else:
#             #     valid = False
#             #     break
#             # if p_idx < len(p):
#             #     pass
#             obj = self.check(p,p_idx,s_idx , s[s_idx], p[p_idx])
#             valid = obj["valid"]
#             p_idx = obj["p_idx"]
#             s_idx = obj["s_idx"]
#         if p_idx == p_len and s_idx != s_len - 1:
#             valid = False
            

        # Check if the remaining characters in pattern are all '*'
        # while p_idx + 1 < len(p) and p[p_idx + 1] == '*':
        #     p_idx += 2

        # return p_idx == len(p) and valid
        # return valid
    
    # def check(self, p:str, p_idx:int,s_idx:int, char1:str, char2:str):
    #     valid = True
    #     print(s_idx,char1,p_idx,char2)
    #     if char1 != char2:
    #         if char2 != "*" and char2 != ".":
    #             p_idx += 1
    #         elif char2 == "*":
    #             obj = self.check(p ,p_idx ,s_idx , char1, p[p_idx - 1])
    #             valid = obj["valid"]
    #             p_idx = obj["p_idx"]
    #             s_idx = obj["s_idx"]
    #         elif char2 == ".":
    #             p_idx += 1
    #             s_idx += 1 
    #     else:
    #         p_idx += 1
    #         s_idx += 1 


    #     return dict(valid = valid,p_idx= p_idx,s_idx=s_idx)

class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        str_len = len(s)
        p_len = len(p)
        s_idx = 0
        p_idx = 0
        valid = True
        
        if str_len != p_len:
            return False

        while s_idx < str_len and p_idx < p_len:
            char1 = s[s_idx]
            char2 = p[p_idx]

            obj = self.check(p, p_idx, char1, char2)
            valid = obj["valid"]
            p_idx = obj["p_idx"]
            if(valid == False):
                return valid
            else:
                s_idx += 1
        return valid
    
    def check(self, p: str, p_idx: int, char1: str, char2: str):
        valid = True
        
        if char1 != char2:
            if char2 != "*" and char2 != ".":
                valid = False
            elif char2 == "*":
                temp_idx = p_idx
                while p_idx < len(p) and p[p_idx] == "*":
                    temp_idx -= 1
                if p_idx < len(p):
                    obj = self.check(p, temp_idx, char1, p[temp_idx])
                    valid = obj["valid"]
                    # p_idx = obj["p_idx"]
                else:
                    valid = False
            elif char2 == ".":
                p_idx += 1
        else:
            p_idx += 1

        return dict(valid=valid, p_idx=p_idx)


# Example usage
s = Solution()
print(s.isMatch("ab", "a*"))
