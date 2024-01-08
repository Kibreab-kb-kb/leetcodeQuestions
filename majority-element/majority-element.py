class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=defaultdict(int)
        n=len(nums)

        for num in nums:
            count[num]+=1
        for key,value in count.items():
            if value>n//2:
                return key