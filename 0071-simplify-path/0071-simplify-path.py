class Solution:
    def simplifyPath(self, path: str) -> str:
        # Use a list as a stack; it is more memory efficient than creating 
        # a new list from split() if the path is extremely long.
        stack = []
        for part in path.split('/'):
            if part == '..':
                if stack: stack.pop()
            elif part and part != '.':
                stack.append(part)
        return "/" + "/".join(stack)