






class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        output = 0
        for i in range(left, right+1):
            output += self.nums[i]
        return output


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



obj = NumArray([-2, 0, 3, -5, 2, -1])

print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))

