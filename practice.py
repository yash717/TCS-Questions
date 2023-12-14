class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the values of Roman numerals
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0  # Initialize the result
        
        prev_value = 0  # Initialize the previous Roman numeral value
        
        for char in s:
            current_value = roman_values[char]
            
            # If the current value is greater than the previous, it's a subtraction case
            if current_value > prev_value:
                total += current_value - 2 * prev_value  # Subtract twice the previous value
            else:
                total += current_value
            
            prev_value = current_value  # Update the previous value
        
        return total
