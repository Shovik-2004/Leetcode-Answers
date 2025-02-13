class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative = x < 0
        
        # Convert to positive for processing
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10
        
        # Apply the original sign
        if negative:
            result = -result
        
        # Check for 32-bit signed integer overflow
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
    
    

        