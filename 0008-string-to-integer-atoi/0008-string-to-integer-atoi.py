class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_number = False   # 숫자가 나왔는가?
        is_positive = True  # 양수인가?
        is_started = False  # 부호든 숫자든 뭔가 시작되었는가? (추가됨)
        result = 0
        
        for char in s:
            if char == " ":
                if is_started:
                    break
                else:
                    continue
            elif char == "-" or char == "+":
                if is_started: 
                    break 
                is_started = True
                if char == "-":
                    is_positive = False
                continue
            elif char.isdigit():
                is_number = True
                is_started = True
                result = result * 10 + int(char)
            else:
                break 

        final_result = result if is_positive else -1 * result
        
        if final_result < -2**31: return -2**31
        if final_result > 2**31 - 1: return 2**31 - 1
            
        return final_result