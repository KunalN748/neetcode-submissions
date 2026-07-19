class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for char in s:
            if char == '[':
                arr.append(']')
            elif char == '{':
                arr.append('}')
            elif char == '(':
                arr.append(')')
            else:
                if len(arr) == 0 or char != arr.pop():
                    return False
        return True if len(arr) == 0 else False