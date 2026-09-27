# Array, Prefix Sum
## 238. Product of Array Except Self

### 접근방법: 누적곱
### 시간복잡도: O(N)
### 공간복잡도: O(N)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        answer = [1] * (len(nums) + 1)

        # 0 1 12 123 1234
        for idx in range(len(nums)):
            answer[idx+1] = answer[idx] * nums[idx]

        print(answer)

        for idx in range(len(nums) - 1, -1, -1):
            answer[idx] *= (answer[idx-1] * nums[idx])

        return answer

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.productExceptSelf([1,2,3,4])
    answer2 = sol.productExceptSelf([-1,1,0,-3,3])

    print(answer1)  # [24,12,8,6]
    print(answer2)  # [0,0,9,0,0]
