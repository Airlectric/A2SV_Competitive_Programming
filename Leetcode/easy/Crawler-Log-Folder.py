class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        commands = {"../","./"}

        for ops in logs:
            if stack and ops == "../":
                stack.pop()
            else:
                if ops not in commands:
                    stack.append(ops)
        
        return len(stack)
        