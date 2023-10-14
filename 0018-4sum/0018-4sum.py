class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        st=set()
        for i in range(n):
            for j in range(i+1,n):
                d=set()
                for k in range(j+1,n):
                    s=nums[i]+nums[j]+nums[k]
                    fourth=target-s
                    if fourth in d:
                        temp=[nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    d.add(nums[k])
        ans=[list(i) for i in st]
        return ans
                    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(n):
            # avoid the duplicates while moving i:
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                # avoid the duplicates while moving j:
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    s=nums[i]+nums[j]+nums[k]+nums[l]
                    if s==target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        # skip the duplicates:
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                    elif s<target:
                        k+=1
                    else:
                        l-=1
        return ans