class Solution:

    def encode(self, strs: List[str]) -> str:
        result = "" 
        for s in strs:
            result += ":"
            for c in s:
                if c == ':':
                    result += "|:"
                elif c == '|':
                    result += "||"
                else:
                    result += c
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        is_special = False
        for c in s:
            if c == ':' and not is_special:
                result.append("")
            elif c == '|' and not is_special:
                is_special = True
            else:
                result[-1] += c
                is_special = False
        return result