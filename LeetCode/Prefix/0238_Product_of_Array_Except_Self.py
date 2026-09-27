# Array, Prefix Sum
## 238. Product of Array Except Self

### 접근방법: 누적곱
### 시간복잡도: O(N)
### 공간복잡도: O(N)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        answer = []

        nums_length = len(nums)

        left = [1 for _ in range(nums_length + 1)]
        right = [1 for _ in range(nums_length + 1)]

        for idx in range(0, len(nums)):
            left[idx+1] = left[idx] * nums[idx]
            right[nums_length - idx - 1] = right[nums_length - idx] * nums[nums_length - idx - 1]

        for idx in range(nums_length):
            answer.append(left[idx] * right[idx+1])

        return answer

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.productExceptSelf([1,2,3,4])
    answer2 = sol.productExceptSelf([-1,1,0,-3,3])

    print(answer1)  # [24,12,8,6]
    print(answer2)  # [0,0,9,0,0]
