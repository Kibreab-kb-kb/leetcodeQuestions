class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        
        for key,value in count.items():
            if value==1:
                return key
