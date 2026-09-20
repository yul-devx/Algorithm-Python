# Array, Hash Table
## 0001. Two Sum

### 접근방법: 완전탐색, 해시테이블
### 시간복잡도: O(N)
### 공간복잡도: O(N)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = {}

        for idx, num in enumerate(nums):
            if(target-num in answer):
                return [answer[target-num], idx]

            answer[num] = idx

        return []

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.twoSum([2,7,11,15], 9)
    answer2 = sol.twoSum([3,2,4], 6)
    answer3 = sol.twoSum([3,3], 6)

    print(answer1)  # [0,1]
    print(answer2)  # [1,2]
    print(answer3)  # [0,1]
