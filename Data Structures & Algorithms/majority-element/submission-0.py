class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = sorted(nums)
        return k[len(nums)//2]
        