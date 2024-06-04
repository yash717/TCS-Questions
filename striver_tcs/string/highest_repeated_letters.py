class Solution:
    def highest_repeated_letters(self, s: str) -> str:
        """
        Find the word in a given string with the highest number of repeated letters.

        Parameters:
            s (str): The input string.

        Returns:
            str: The word with the highest number of repeated letters. If not found, returns -1.
        """
        # Initialize variables to store the result
        maximum_word = 0
        result = ""

        # Split the string into words
        words = s.split()

        # Iterate over each word in the string
        for word in words:
            # Initialize an array to store the frequency of each letter
            frequency = [0] * 26
            curr_maximum_word = 0

            # Calculate the frequency of each letter in the current word
            for char in word:
                if char.isalpha():
                    frequency[ord(char.lower()) - ord('a')] += 1

            # Check the frequency of each letter
            for freq in frequency:
                if freq > 1:
                    curr_maximum_word += 1

            # Update the result if the current word has more repeated letters
            if curr_maximum_word > maximum_word:
                maximum_word = curr_maximum_word
                result = word

        # Return the result
        if maximum_word == 0:
            return "-1"
        else:
            return result


# Test cases
s1 = "abcdefg google microsoft"
print("\nExample 1:")
print("Input:", s1)
print("Output:", Solution().highest_repeated_letters(s1))  # Output: google

s2 = "cameron blue"
print("\nExample 2:")
print("Input:", s2)
print("Output:", Solution().highest_repeated_letters(s2))  # Output: -1
