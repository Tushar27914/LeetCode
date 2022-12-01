class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        stack=[]
        for char in path:
            if char:
                if char == '..':
                    stack=stack[:-1]
                elif char != '.':
                    stack.append(char)
        return '/'+'/'.join(stack)
                
            
        