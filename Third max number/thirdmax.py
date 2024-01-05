class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=set(nums)
        list1=sorted(a,reverse=True)

        if len(list1)>=3:
            return list1[2]
        else:
            return max(list1)