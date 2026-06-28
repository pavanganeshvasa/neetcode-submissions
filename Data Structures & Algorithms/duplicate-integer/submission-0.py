class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set()
        for i in range(len(nums)):
            nums1.add(nums[i])

        return len(nums) != len(nums1)


        