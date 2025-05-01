class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        stack = []
        commands = [' ','.','..']

        for char in path:
            if char and char not in commands:
                stack.append(char)
            elif stack and char == '..':
                stack.pop()

        return '/' + '/'.join(stack)
            
        