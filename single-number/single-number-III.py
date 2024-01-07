class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        res=[]
        for key,value in count.items():
            if value==1:
                res.append(key)
        return res
        