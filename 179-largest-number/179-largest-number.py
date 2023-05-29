# class Solution:
#     def largestNumber(nums):
    
#         nums = [str(num) for num in nums]

    
#         def compare(x, y):
#             return int(y + x) - int(x + y)


#         nums.sort(key=compare)


#         if nums[0] == '0':
#             return '0'
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


        # return ''.join(nums)
