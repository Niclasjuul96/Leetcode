from ast import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the occurrences of each number
        num_counts = Counter(nums)

        # Sort the numbers based on their frequencies in descending order
        sorted_nums = sorted(num_counts.keys(), key=lambda x: num_counts[x], reverse=True)

        # Return the top k frequent numbers
        return sorted_nums[:k]
        