# Array, Hash Table, Divide and Conquer, Sorting, etc ...
## 347. Top K Frequent Elements

### 접근방법: 해시, 정렬
### 시간복잡도: O(N x logN)
### 공간복잡도: O(N)

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        answer = sorted(num_dict, key=lambda x:num_dict[x], reverse=True)

        return answer[:k]

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.topKFrequent([1,1,1,2,2,3], 2)
    answer2 = sol.topKFrequent([1], 1)
    answer3 = sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)

    print(answer1)  # [1,2]
    print(answer2)  # [1]
    print(answer3)  # [1,2]
