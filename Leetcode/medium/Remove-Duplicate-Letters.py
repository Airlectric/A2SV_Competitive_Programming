class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = set()
        count = {}
        stack = []

        for let in s:
            count[let] = count.get(let,0) + 1

        for let in s:
            count[let] -= 1

            if let in visited:
                continue

            while stack and let < stack[-1] and count[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(let)
            visited.add(let)

        return ''.join(stack)
        