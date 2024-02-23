class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charStack = []
        valid = True
        for i in s:
            if i == "{" or i == "[" or i == "(":
                charStack.append(i)
                print(charStack[-1])
            elif i == "}":
                if charStack[-1] != "{" and i == "}":
                    valid = False
            elif i == "]":
                if charStack[-1] != "[" and i == "]":
                    print(charStack[-1])
                    valid = False
            elif i == ")":
                if charStack[-1] != "(" and i == ")":
                    valid = False
                
        
        return(valid)
            

if __name__ == '__main__':
    solution = Solution()
   
    print(solution.isValid("(]"))
