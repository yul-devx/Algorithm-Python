# Array, Two Pointers
## 238. Move Zeroes

### 접근방법: 
### 시간복잡도: O(n)
### 공간복잡도: O(n)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for idx in range(len(nums)-1):
            print(idx)
            if nums[idx] == 0:
                nums.pop(0)
                nums.append(0)
        
        print(nums)


if __name__ == "__main__":

    sol = Solution()

    # answer1 = sol.moveZeroes([0,1,0,3,12])
    # answer2 = sol.moveZeroes([0])
    answer3 = sol.moveZeroes([0,0,1])

    # print(answer1)  # [1,3,12,0,0]
    # print(answer2)  # [0]
    print(answer3)  # [1,0,0]
