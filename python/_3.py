class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        This function uses a sliding window approach with a set to keep track of 
        characters within the current window.

        The algorithm works as follows:
        1. Initialize a set (`char_set`) for the current window's characters, 
           `left` (the start of the window), and `max_length` (the longest 
           found length).
        2. Iterate through the string with `right` (the end of the window).
        3. **Sliding:** If the character $s[\text{right}]$ is already in 
           `char_set`, shrink the window from the `left` by removing 
           $s[\text{left}]$ from `char_set` and incrementing `left` until 
           $s[\text{right}]$ is no longer a duplicate.
        4. **Expansion:** Add $s[\text{right}]$ to `char_set` to expand the window.
        5. **Update Max:** Calculate the current window length 
           ($\text{right} - \text{left} + 1$) and update `max_length`.
        6. Return `max_length` after iterating through the entire string.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.

        Raises:
            TypeError: If the input `s` is not a string (though the type hint
                       implies it should be handled).

        Examples:
            >>> sol = Solution()
            >>> sol.lengthOfLongestSubstring("abcabcbb")
            3
            >>> sol.lengthOfLongestSubstring("bbbbb")
            1
            >>> sol.lengthOfLongestSubstring("pwwkew")
            3
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