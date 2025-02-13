class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of Roman numeral symbols to their corresponding values
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        # Resultant Roman numeral string
        roman = []
        
        # Iterate over the value-symbol pairs
        for value, symbol in value_symbols:
            # While the current value can be subtracted from num
            while num >= value:
                # Append the corresponding Roman numeral symbol
                roman.append(symbol)
                # Subtract the current value from num
                num -= value
        
        # Join and return the resultant list as a string
        return ''.join(roman)