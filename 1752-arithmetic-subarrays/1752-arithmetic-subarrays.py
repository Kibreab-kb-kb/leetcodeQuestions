class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        c = []
        for i in range(len(l)):
            a = sorted(nums[l[i]:r[i]+1])
            b = []
            for j in range(len(a)-1):
                b.append(abs(a[j]-a[j+1]))
            c.append(len(set(b))==1)
        return c