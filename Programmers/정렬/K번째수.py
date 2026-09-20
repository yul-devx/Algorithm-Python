# 정렬
## K번째수

### 접근방법: 배열 슬라이싱, 정렬
### 시간복잡도: O(M x NlogN)
### 공간복잡도: O(N + M)

def solution(array, commands):
    answer = []

    for (i, j, k) in commands:
        answer.append(sorted(array[i-1:j])[k-1])

    return answer   

if __name__ == "__main__":
    answer1 = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	)

    print(answer1)    # [5, 6, 3]