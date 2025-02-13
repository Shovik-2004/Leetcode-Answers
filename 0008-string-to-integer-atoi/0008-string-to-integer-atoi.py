class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i].isspace():
            i += 1
        
        # Step 2: Check for optional sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Convert digits to integer
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow and clamp if necessary
            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX
            
            result = result * 10 + digit
            i += 1
        
        # Apply the sign
        result *= sign
        
        # Step 4: Return the final result
        return result

        