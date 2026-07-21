class Solution:
    def romanToInt(self, s: str) -> int:
        my_symbols = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        result = 0
        # for letter in s:
        #     result += my_simpols[letter]
        # if "IV" in s:
        #     result -= 1 * 2
        # if "IX" in s:
        #     result -= 1 * 2
        # if "XL" in s:
        #     result -= 10 * 2
        # if "XC" in s:
        #     result -= 10 * 2
        # if "CD" in s:
        #     result -= 100 * 2
        # if "CM" in s:
        #     result -= 100 * 2
          
        # return result

        for i in range(len(s) - 1):
            if my_symbols[s[i]] < my_symbols[s[i + 1]]:
                result -= my_symbols[s[i]]
            else:
                result += my_symbols[s[i]]

        result += my_symbols[s[-1]]

        return result