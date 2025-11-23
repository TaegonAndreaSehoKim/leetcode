class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        while num > 0:
            while num >= 1000:
                result += "M"
                num = num - 1000
            while num >= 900:
                result += "CM"
                num = num - 900
            while num >= 500:
                result += "D"
                num = num - 500
            while num >= 400:
                result += "CD"
                num = num - 400
            while num >= 100:
                result += "C"
                num = num - 100
            while num >= 90:
                result += "XC"
                num = num - 90
            while num >= 50:
                result += "L"
                num = num - 50
            while num >= 40:
                result += "XL"
                num = num - 40
            while num >= 10:
                result += "X"
                num = num - 10
            while num >= 9:
                result += "IX"
                num = num - 9
            while num >= 5:
                result += "V"
                num = num - 5
            while num >= 4:
                result += "IV"
                num = num - 4
            while num >= 1:
                result += "I"
                num = num - 1
        return result