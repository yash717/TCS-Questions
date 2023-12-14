class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the input string 's' into words while filtering out empty strings
        words = s.split()

        # Reverse the order of words
        reversed_words = words[::-1]

        # Join the reversed words into a single string with a single space between them
        reversed_string = ' '.join(reversed_words)

        return reversed_string
