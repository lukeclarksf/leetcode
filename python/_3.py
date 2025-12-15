class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Finds the length of the longest substring in the given string $s$ without repeating characters.

        This is solved efficiently using the sliding window approach. A set, `char_set`, is used to keep track
        of characters within the current window defined by the two pointers, `left` and `right`. As the
        `right` pointer advances, the character is added to the set. If the character is already present
        in the set, the `left` pointer is moved forward and characters are removed from the set until
        the window contains only unique characters again. The maximum length is calculated at each step.
        

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            
        return max_length