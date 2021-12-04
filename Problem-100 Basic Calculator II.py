# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/

# Logic: We iterate over the input string. We have a lastsign and 
# a num variable to store the current number and last sign encountered. 
# When we reach a sign, we make number 0 and if it is + or - we push 
# the same into the stack. If the lastsign is / or *, we pop from stack 
# and do operation then push back into thte stack. At the end we return 
# the sum of all the elements in the stack.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def calculate(self, s: str) -> int:
        stack = list()
        ops = ['/', '*', '+', '-']
        
        lastSign = '+'
        num = 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            
            if s[i] in ops or i == len(s) - 1:
                if lastSign == '+':
                    stack.append(num)
                elif lastSign == '-':
                    stack.append(-num)
                elif lastSign == '*':
                    stack.append(stack.pop()*num)
                elif lastSign == '/':
                    stack.append(int(stack.pop()/num))
                
                num = 0
                lastSign = s[i]
        
        return sum(stack)
