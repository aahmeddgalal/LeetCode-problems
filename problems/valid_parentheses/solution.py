class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        for char in s:
            if char in "([{":
                stack.append(char)
            if char in ")}]":
                if stack == []:
                    return False
                last = stack.pop()
                if last != pairs[char]:
                    return False 
        if stack == []:
            return True
        return False
