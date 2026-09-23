class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_str = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_str = ""
                current_num = 0

            elif char == ']':
                k = num_stack.pop()
                prev = str_stack.pop()
                current_str = prev + k * current_str

            else:
                current_str += char
            
        return current_str