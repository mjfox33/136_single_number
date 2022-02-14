class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        found = set()
        for i in nums:
            if i in found:
                found.remove(i)
                continue
            found.add(i)
        return found.pop()