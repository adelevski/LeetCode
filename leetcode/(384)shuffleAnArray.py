from typing import List
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.copy = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.copy[:]
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)
        for i in range(n):
            j = randint(i, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


nums = [1, 2, 3, 4, 5, 6]
# Your Solution object will be instantiated and called as such:
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())