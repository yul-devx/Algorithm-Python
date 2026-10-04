# Array, Prefix Sum
## 238. Product of Array Except Self

### 접근방법: 누적곱
### 시간복잡도: O(N)
### 공간복잡도: O(1)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        answer = [1] * len(nums)

        left = 1
        for idx in range(len(nums)):
            answer[idx] = left
            left *= nums[idx]

        """
        [
            1, 
            1*nums[0], 
            1*nums[0]*nums[1], 
            1*nums[0]*nums[1]*num[2]
        ]
        """

        right = 1
        for idx in range(len(nums) - 1, -1, -1):
            answer[idx] *= right
            right *= nums[idx]

        """
        [
            1 *1*nums[3]*nums[2]*nums[1], 
            1*nums[0] *1*nums[3]*nums[2], 
            1*nums[0]*nums[1] *1*nums[3], 
            1*nums[0]*nums[1]*num[2] *1,
        ]
        """

        return answer

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.productExceptSelf([1,2,3,4])
    answer2 = sol.productExceptSelf([-1,1,0,-3,3])

    print(answer1)  # [24,12,8,6]
    print(answer2)  # [0,0,9,0,0]
