class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Finds two numbers in the input list that add up to the target value.

        This method uses a hash map (dictionary) to efficiently store numbers encountered 
        and their indices, allowing for an $O(n)$ time complexity solution by checking 
        if the required complement ($target - current\ number$) already exists in the map 
        during a single pass through the list.

        Args:
            nums: A list of integers to search through.
            target: The integer target sum.

        Returns:
            A list containing the indices of the two numbers that sum up to the target. 
            Returns an empty list if no such pair is found.
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []