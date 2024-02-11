class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prefix_dict = {}
        postfix_dict = {}
        ans_arr = [0] * len(nums)

        for i in range(len(nums)):
            # prefix dict
            if nums[i] not in prefix_dict:
                prefix_dict[nums[i]] = (i, 1)
                ans_arr[i] -= i
            else:
                prevSum, occur = prefix_dict[nums[i]]
                ans_arr[i] += i*(occur) - (prevSum + i)
                prefix_dict[nums[i]] = (prevSum + i, occur + 1)

            # postfix dict
            reverse_i = len(nums) - i - 1
            if nums[reverse_i] not in postfix_dict:
                postfix_dict[nums[reverse_i]] = (reverse_i, 1)
                ans_arr[reverse_i] += reverse_i
            else:
                postSum, ocuur_rev = postfix_dict[nums[reverse_i]]
                ans_arr[reverse_i] += (postSum + reverse_i) - reverse_i*(ocuur_rev)
                postfix_dict[nums[reverse_i]] = (postSum + reverse_i, ocuur_rev + 1)
        
        return ans_arr
