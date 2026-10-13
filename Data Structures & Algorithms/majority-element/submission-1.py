class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        e = Counter(nums)
        res = nums[0]
        m = 0
        for k,v in e.items():
            if v>m:
                res = k
                m=v
        return res

        