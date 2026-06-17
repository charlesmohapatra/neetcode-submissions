class Solution:
    def hf(self,s: str) -> str:
        match s:
            case "(":
                return ")"
            case "[":
                return "]"
            case "{":
                return "}"
        return ""
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        else:
            stack = []
            for i in s:
                if i in '([{':
                    stack.append(i)
                else:
                    if not stack or self.hf(stack.pop()) != i:
                        return False
            return not stack


        