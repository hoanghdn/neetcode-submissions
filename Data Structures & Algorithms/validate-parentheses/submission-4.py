class Solution:
    def isValid(self, s: str) -> bool:
        openers = ['(','{','[']
        closers = [')','}',']']
        curr_stack = []

        for char in s:
            if char in openers:
                curr_stack.append(char)
            elif char in closers:
                if not curr_stack:
                    return False
                if char == ')' and curr_stack.pop() == '(':
                    continue
                elif char == '}' and curr_stack.pop() == '{':
                    continue
                elif char == ']' and curr_stack.pop() == '[':
                    continue
                else:
                    return False
        return not curr_stack
            
        
