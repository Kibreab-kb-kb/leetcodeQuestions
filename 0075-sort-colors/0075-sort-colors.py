class Solution:
    def sortColors(self, nums):
        red_ptr, blue_ptr = 0, len(nums) - 1
        curr_ptr = 0

        while curr_ptr <= blue_ptr:
            if nums[curr_ptr] == 0:
                nums[curr_ptr], nums[red_ptr] = nums[red_ptr], nums[curr_ptr]
                red_ptr += 1
                curr_ptr += 1
            elif nums[curr_ptr] == 2:
                nums[curr_ptr], nums[blue_ptr] = nums[blue_ptr], nums[curr_ptr]
                blue_ptr -= 1
            else:
                curr_ptr += 1
