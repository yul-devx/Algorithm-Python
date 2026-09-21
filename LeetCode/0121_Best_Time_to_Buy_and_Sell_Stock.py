# Array, Dynamic Pgramming
## 121.Best TIime to Buy and Sell Stock

### 접근방법: 
### 시간복잡도: O(n)
### 공간복잡도: O(n)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_num = prices[0]
        max_num = prices[0]
        answer = 0

        for num in prices:

            if (num < min_num):
                min_num = num
                max_num = num

            if (num > max_num):
                max_num = num

            answer = max_num - min_num

        return answer

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.maxProfit([7,1,5,3,6,4])
    answer2 = sol.maxProfit([7,6,4,3,1])
    answer3 = sol.maxProfit([2,4,1])

    print(answer1)  # 5
    print(answer2)  # 0
    print(answer3)  # 2
