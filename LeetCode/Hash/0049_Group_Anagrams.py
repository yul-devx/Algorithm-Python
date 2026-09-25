# Array, Hash Table, String, Sorting
## Group Anagrams

### 접근방법: 해시, 정렬, 문자열
### 시간복잡도: O(N x KlogK)
### 공간복잡도: O(N x K)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        word_dict = {}

        for word in strs:
            word_dict.setdefault(tuple(sorted(word)), []).append(word)

        return list(word_dict.values())

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    answer2 = sol.groupAnagrams([""])
    answer3 = sol.groupAnagrams(["a"])

    print(answer1)  # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(answer2)  # [[""]]
    print(answer3)  # [["a"]]
